FROM python:3.11-slim

# Build arguments
ARG STOCKFISH_VERSION=latest
ARG STOCKFISH_BUILD=ubuntu-x86-64-avx2

# System dependencies
RUN apt-get update && apt-get install -y \
        wget \
        tar \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Download and install Stockfish
RUN wget -O stockfish.tar "https://github.com/official-stockfish/Stockfish/releases/${STOCKFISH_VERSION}/download/stockfish-${STOCKFISH_BUILD}.tar" && \
    tar -xf stockfish.tar && \
    mv stockfish /usr/local/bin/stockfish && \
    chmod +x /usr/local/bin/stockfish && \
    rm stockfish.tar

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

# Default command
CMD ["python", "stockfish"]