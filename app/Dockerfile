# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Avoid Python writing .pyc files and buffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirement list and install Python deps
COPY requirements.txt .

# Ensure /.local exists and is writable
RUN mkdir -p /.local && chmod -R 777 /.local

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --break-system-packages -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 8080

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
