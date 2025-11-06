# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Avoid Python writing .pyc files and buffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment and activate it
RUN python -m venv /app/venv

# Ensure venv is used by default
ENV PATH="/app/venv/bin:$PATH"

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose port
EXPOSE 8080

# Run app from virtual environment
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
