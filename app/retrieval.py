import os
from pinecone import Pinecone
from app.embeddings import get_embedding

PINECONE_API_KEY =os.getenv("PINECONE_API_KEY")
PINECONE_ENV = "us-east1-gcp"
INDEX_NAME = "docker-index"

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

def retrieve_context(query, top_k=5):
    query_embedding = get_embedding(query)

    response = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    contexts = []
    for match in response["matches"]:
        contexts.append(match["metadata"]["text"])

    return contexts

from app.llm import generate_answer

def rag_answer(query: str, top_k: int = 5) -> str:
    chunks = retrieve_context(query, top_k=top_k)

    context = "\n\n".join(chunks[:3])

    return generate_answer(query, context)
