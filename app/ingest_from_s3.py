import os
import uuid
import boto3
from io import BytesIO
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from botocore.exceptions import ClientError, NoCredentialsError
from dotenv import load_dotenv
load_dotenv()


# --------------------
# Config
# --------------------
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
PREFIX = "pdfs/"

if not BUCKET_NAME:
    raise RuntimeError("S3_BUCKET_NAME is not set in environment variables")

# AWS (CLI / IAM Role)
s3 = boto3.client("s3")

# Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

# Embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def ingest_from_s3():
    try:
        response = s3.list_objects_v2(
            Bucket=BUCKET_NAME,
            Prefix=PREFIX
        )

        if "Contents" not in response:
            print("No PDFs found in S3 bucket.")
            return

        for obj in response["Contents"]:
            key = obj["Key"]

            if not key.lower().endswith(".pdf"):
                continue

            print(f"Processing {key}")

            pdf_obj = s3.get_object(Bucket=BUCKET_NAME, Key=key)
            pdf_bytes = pdf_obj["Body"].read()

            reader = PdfReader(BytesIO(pdf_bytes))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)

            chunks = [
                text[i:i + 500]
                for i in range(0, len(text), 400)
            ]

            embeddings = embedder.encode(chunks)

            vectors = []
            for chunk, emb in zip(chunks, embeddings):
                vectors.append({
                    "id": str(uuid.uuid4()),
                    "values": emb.tolist(),
                    "metadata": {
                        "text": chunk,
                        "source": key
                    }
                })

            index.upsert(vectors)
            print(f"Ingested {len(vectors)} chunks from {key}")

    except NoCredentialsError:
        raise RuntimeError("AWS credentials not found. Run `aws configure`.")

    except ClientError as e:
        raise RuntimeError(f"S3 ingestion failed: {e}")


if __name__ == "__main__":
    ingest_from_s3()
