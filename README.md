
# 📄 RAG-based PDF Question Answering System

A **production-ready Retrieval-Augmented Generation (RAG) system** that enables users to upload PDFs and ask natural language questions. The system retrieves relevant context using **semantic search** and generates **accurate, grounded answers** using a **Groq-hosted LLaMA 3.1 model**, exposed via an interactive **Streamlit UI**.

---

## 🚀 Features

* Upload and process PDF documents
* Intelligent text chunking and embedding generation
* Semantic search using **Pinecone vector database**
* Context-aware answer generation using **LLaMA 3.1 (Groq)**
* Interactive and user-friendly **Streamlit UI**
* Reduced hallucinations through retrieval-based grounding

---

## 🧠 System Architecture

```
PDF Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embedding Generation
   ↓
Pinecone Vector Store
   ↓
Semantic Retrieval
   ↓
Context + Query
   ↓
Groq LLaMA 3.1
   ↓
Answer Generation
```

---

## 🛠️ Tech Stack

**Backend & AI**

* Python
* Retrieval-Augmented Generation (RAG)
* Groq-hosted **LLaMA 3.1**
* Embeddings for semantic search

**Vector Database**

* Pinecone

**Frontend**

* Streamlit

**Document Processing**

* PDF text extraction
* Chunking & preprocessing

---

## ⚙️ How It Works

1. **PDF Processing**
   Uploaded PDFs are parsed and converted into raw text.

2. **Chunking & Embeddings**
   Text is split into manageable chunks and converted into embeddings.

3. **Vector Storage**
   Embeddings are stored in **Pinecone**, enabling fast semantic similarity search.

4. **Query Handling**
   User queries are embedded and matched against stored vectors.

5. **Context Retrieval**
   Most relevant chunks are retrieved using semantic search.

6. **Answer Generation**
   Retrieved context is passed to **LLaMA 3.1 (Groq)** to generate accurate, grounded responses.

---

## 📌 Why RAG?

* Prevents hallucinations by grounding responses in real documents
* Scales efficiently for large document sets
* Provides explainable, context-aware answers
* Suitable for enterprise knowledge bases and document intelligence systems

---

## 🖥️ User Interface

* Simple PDF upload
* Natural language question input
* Real-time AI-generated responses
* Clean and intuitive Streamlit layout

---

## 📦 Installation & Setup (High-Level)

```bash
git clone https://github.com/harshadakhorgade/rag_prod
cd rag_prod
pip install -r requirements.txt
streamlit run app.py
```

> Ensure Pinecone and Groq API keys are configured as environment variables.

---

## 🔮 Future Enhancements

* Multi-PDF querying
* Chat history and memory
* Source citations in responses
* Authentication and role-based access
* Cloud deployment (AWS / Docker)

---

## 👤 Author

**Harshada Kailas Khorgade**
📧 [harshadakhorgade37@gmail.com](mailto:harshadakhorgade37@gmail.com)
🔗 GitHub: [https://github.com/harshadakhorgade](https://github.com/harshadakhorgade)

---


