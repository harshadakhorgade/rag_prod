FROM python:3.11-slim

WORKDIR /app

# System deps (recommended for ML)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Upgrade pip and install CPU-only Torch first, then the rest of requirements
RUN pip install --upgrade pip \
    && pip install --no-cache-dir torch==2.9.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
