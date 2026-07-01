FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
        git \
        build-essential \
        pkg-config \
        libssl-dev \
        curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir "git+https://github.com/headroomlabs-ai/headroom.git@v0.27.0"

COPY . .

EXPOSE 8000

CMD ["sh","-c","uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
