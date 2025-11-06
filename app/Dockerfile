# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Avoid Python writing .pyc files and buffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set HOME to a writable directory (prevents /.local issue)
ENV HOME=/root
ENV PATH="$HOME/.local/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .

# Force pip to install globally (never in /.local)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --root=/usr/local -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 8080

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
