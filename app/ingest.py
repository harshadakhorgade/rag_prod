from pathlib import Path
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from dotenv import load_dotenv
import os
import uuid

# ---------- CONFIG ----------
PDF_DIR = Path("data/docs")
EMBED_MODEL = "all-MiniLM-L6-v2"

load_dotenv()

# ---------- LOAD ----------
print("Loading embedding model...")
embedder = SentenceTransformer(EMBED_MODEL)

print("Connecting to Pinecone...")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

# ---------- UTILS ----------
def read_pdf(file_path: Path) -> str:
    reader = PdfReader(file_path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def chunk_text(text, size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks

# ---------- INGEST ----------
def ingest():
    vectors = []

    for pdf in PDF_DIR.glob("*.pdf"):
        print(f"Processing {pdf.name}")
        text = read_pdf(pdf)
        chunks = chunk_text(text)
        embeddings = embedder.encode(chunks)

        for chunk, emb in zip(chunks, embeddings):
            vectors.append({
                "id": str(uuid.uuid4()),
                "values": emb.tolist(),
                "metadata": {
                    "text": chunk,
                    "source": pdf.name
                }
            })

    index.upsert(vectors=vectors)
    print(f"Ingested {len(vectors)} chunks into Pinecone")

if __name__ == "__main__":
    ingest()
