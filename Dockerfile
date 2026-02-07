FROM python:3.11-slim

# System dependencies
RUN apt-get update && apt-get install -y \
        wget \
        tar \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Download and install Stockfish
RUN apt-get update && apt-get install -y wget tar ca-certificates && \
    wget https://github.com/official-stockfish/Stockfish/releases/latest/download/stockfish-ubuntu-x86-64-avx2.tar && \
    tar -xf stockfish-ubuntu-x86-64-avx2.tar && \
    mv stockfish/stockfish-ubuntu-x86-64-avx2 /usr/local/bin/stockfish && \
    chmod +x /usr/local/bin/stockfish && \
    rm -rf stockfish stockfish-ubuntu-x86-64-avx2.tar

# Confirm Stockfish installation
RUN which stockfish

# App setup
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Ingestion/ Ingestion/
COPY Processing/ Processing/
COPY Analysis/ Analysis/
COPY Querying/ Querying/

# Mount points (volumes at runtime)
RUN mkdir Data Reports
RUN mkdir -p /app/Data/Bronze /app/Data/Silver /app/Data/Gold

# Run pipeline on container start
CMD ["python", "-m","Analysis.bkchessma_2024p_ingest"]