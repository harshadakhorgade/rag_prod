from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import rag_answer
from fastapi import UploadFile, File
from app.s3_utils import upload_pdf


app = FastAPI(title="RAG Chatbot API")

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = rag_answer(request.question)
    return {"answer": answer}

@app.post("/upload-pdf")
def upload_pdf_endpoint(file: UploadFile = File(...)):
    s3_path = upload_pdf(file.file, file.filename)
    return {"message": "Uploaded", "path": s3_path}