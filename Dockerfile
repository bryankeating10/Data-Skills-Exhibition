FROM python:3.11-slim

# Build arguments
ARG STOCKFISH_VERSION=17.1
ARG STOCKFISH_BUILD=linux_x64_avx2

# System dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Stockfish
RUN wget https://stockfishchess.org/files/stockfish_${STOCKFISH_VERSION}_${STOCKFISH_BUILD}.zip && \
    unzip stockfish_${STOCKFISH_VERSION}_${STOCKFISH_BUILD}.zip && \
    mv stockfish_${STOCKFISH_VERSION}/stockfish /usr/local/bin/stockfish && \
    chmod +x /usr/local/bin/stockfish && \
    rm -rf stockfish_${STOCKFISH_VERSION}_${STOCKFISH_BUILD}.zip stockfish_${STOCKFISH_VERSION}

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
CMD ["python", "Analysis/main.py"]