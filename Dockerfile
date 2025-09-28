# FROM python:3.8-slim-bookworm
# WORKDIR /app
# COPY . /app
# RUN apt update -y && apt install -y awscli
# RUN pip install -r requirements.txt
# CMD ["python", "app.py"]
FROM python:3.8-slim-bookworm

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install required packages for apt and awscli
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        awscli \
        curl \
        ca-certificates \
        gnupg \
        lsb-release \
        sudo \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Set default command
CMD ["python", "app.py"]


