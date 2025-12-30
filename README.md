Below is an **updated and polished README section**, with **Amazon S3 explicitly included for PDF storage**, while keeping everything else intact and production-oriented. You can **replace your existing README with this version**.

---

# 📄 RAG-based PDF Question Answering System

A **production-ready Retrieval-Augmented Generation (RAG) system** that enables users to upload PDFs and ask natural language questions. PDFs are securely stored in **Amazon S3**, relevant context is retrieved using **semantic search**, and **accurate, grounded answers** are generated using a **Groq-hosted LLaMA 3.1 model**, exposed via an interactive **Streamlit UI**.

---

## 🚀 Features

* Upload and process PDF documents
* **Secure PDF storage using Amazon S3**
* Intelligent text chunking and embedding generation
* Semantic search using **Pinecone vector database**
* Context-aware answer generation using **LLaMA 3.1 (Groq)**
* Interactive and user-friendly **Streamlit UI**
* Reduced hallucinations through retrieval-based grounding

---

## 🧠 System Architecture

```
PDF Upload (UI)
   ↓
Amazon S3 (PDF Storage)
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

### **Backend & AI**

* Python
* Retrieval-Augmented Generation (RAG)
* Groq-hosted **LLaMA 3.1**
* Embeddings for semantic search

### **Cloud & Storage**

* **Amazon S3** – PDF document storage

### **Vector Database**

* Pinecone

### **Frontend**

* Streamlit

### **Document Processing**

* PDF text extraction
* Chunking & preprocessing

---

## ⚙️ How It Works

1. **PDF Upload & Storage**
   Uploaded PDFs are stored securely in an **Amazon S3 bucket**, enabling scalable and durable document storage.

2. **PDF Processing**
   Stored PDFs are fetched from S3 and parsed into raw text.

3. **Chunking & Embeddings**
   Text is split into manageable chunks and converted into embeddings.

4. **Vector Storage**
   Embeddings are stored in **Pinecone**, enabling fast semantic similarity search.

5. **Query Handling**
   User queries are embedded and matched against stored vectors.

6. **Context Retrieval**
   Most relevant chunks are retrieved using semantic search.

7. **Answer Generation**
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

### Environment Variables Required

```env
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_S3_BUCKET_NAME=your_bucket
PINECONE_API_KEY=your_key
GROQ_API_KEY=your_key
```

---



---

# 🚀 Deployment Guide — Docker + AWS EC2 + ECR

This project is a **Dockerized RAG-based chatbot** deployed using **AWS EC2 and Amazon ECR**.
The application runs with **FastAPI** and exposes Swagger UI at `/docs`.

> **Note:** Docker image builds successfully locally. Deployment on EC2 was partially completed and intentionally paused to avoid unnecessary AWS costs.

---

## ✅ Prerequisites

* AWS Account
* Docker installed locally
* AWS CLI configured locally
* S3 bucket already created (used for PDF ingestion)
* Application runs locally using Docker
* ECR repository created

---

## 🧱 Architecture Overview

* **FastAPI** application
* **Docker** for containerization
* **Amazon ECR** for container registry
* **Amazon EC2 (Ubuntu)** for deployment
* **S3** for document storage
* **Pinecone** for vector database
* **Groq API** for LLM inference

---

## ✅ Steps Completed So Far

### STEP 1 — Dockerize the Application (Local)

* Created `Dockerfile`
* Verified container runs locally
* Swagger UI accessible at:

```
http://localhost:8000/docs
```

---

### STEP 2 — Build Docker Image (Local)

```bash
docker build -t rag-chatbot .
```

Verify:

```bash
docker images
```

---

### STEP 3 — Create Amazon ECR Repository

* Repository name:

```
rag-chatbot
```

* Visibility: **Private**
* Tag mutability: **Mutable**

AWS auto-generated repository URI:

```
590184012044.dkr.ecr.us-east-1.amazonaws.com/rag-chatbot
```

---

### STEP 4 — Launch EC2 Instance

* **AMI**: Ubuntu 24.04 LTS
* **Instance type**: `t2.micro` (⚠️ later found insufficient for ML workloads)
* **Storage**: Initially 8 GB → increased to **15 GB**
* **Security Group**:

  * SSH (22)
  * Custom TCP (8000)

---

### STEP 5 — Install Docker on EC2

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```

---

### STEP 6 — Install AWS CLI v2 on EC2

Used official installer (required for Ubuntu 24.04):

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscliv2.zip
unzip awscliv2.zip
sudo ./aws/install
```

Verified:

```bash
aws --version
```

---

### STEP 7 — Configure AWS Permissions

* IAM user: `rag_user`
* Attached policy:

```
AmazonEC2ContainerRegistryFullAccess
```

Verified identity:

```bash
aws sts get-caller-identity
```

---

### STEP 8 — Login to ECR (EC2)

```bash
aws ecr get-login-password --region us-east-1 \
| docker login \
--username AWS \
--password-stdin 590184012044.dkr.ecr.us-east-1.amazonaws.com
```

✅ Login succeeded.

---

### STEP 9 — Disk Space Issues Encountered (Important)

While building the Docker image on EC2, repeated errors occurred:

```
ERROR: [Errno 28] No space left on device
```

#### Root causes identified:

* EC2 instance type too small for ML dependencies
* PyTorch + NVIDIA CUDA packages consume multiple GB
* Docker layers stored in `/var/lib/docker`

#### Fixes applied:

* Increased EC2 volume from **8 GB → 15 GB**
* Ran Docker cleanup:

```bash
docker system prune -af
docker volume prune -f
```

* Verified expanded disk:

```bash
df -h
```

---

### STEP 10 — PyTorch Dependency Issue

* `torch==2.9.x` attempted to install **GPU CUDA packages**
* CUDA wheels caused disk exhaustion even after cleanup

📌 **Decision taken**:
Deployment paused to avoid:

* Higher EC2 costs
* Unnecessary GPU dependencies on CPU instance

---

## 🛑 Deployment Paused (Intentional)

Deployment was stopped at this point because:

* `t2.micro` is not suitable for ML workloads
* PyTorch CUDA dependencies are very large
* Continuing would require:

  * `t3.medium` or higher
  * CPU-only PyTorch
  * Optimized `requirements.txt`

---

## 🔜 Next Steps (Planned)

When resuming deployment:

1. Use **t3.medium or t3.large**
2. Switch to **CPU-only PyTorch**
3. Rebuild Docker image locally
4. Push image to ECR
5. Pull and run container on EC2
6. Expose application on port `8000`

---

## ✅ Current Application Status

* ✅ Application runs locally in Docker
* ✅ Swagger UI available at `/docs`
* ✅ ECR repository created
* ✅ EC2 setup completed
* ⚠️ Deployment paused due to cost & optimization considerations

---

## 🧠 Key Learnings

* ML containers require **larger EC2 instances**
* PyTorch CUDA wheels are **not suitable for small instances**
* Docker disk usage must be monitored on EC2
* ECR + Docker + EC2 flow validated end-to-end

---









## 🔮 Future Enhancements

* Multi-PDF querying
* Chat history and memory
* Source citations in responses
* Authentication and role-based access
* Full AWS deployment (ECS / EKS / Docker)

---

## 👤 Author

**Harshada Kailas Khorgade**
📧 [harshadakhorgade37@gmail.com](mailto:harshadakhorgade37@gmail.com)
🔗 GitHub: [https://github.com/harshadakhorgade](https://github.com/harshadakhorgade)

---


Just tell me.
