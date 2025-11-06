# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Avoid Python writing .pyc files and buffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Disable pip’s user install fallback (causes /.local issue)
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_ROOT_USER_ACTION=ignore

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# ✅ Force pip to install globally into /usr/local
RUN python -m pip install --upgrade pip

RUN HOME=/root python -m pip install --no-cache-dir --user -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 8080

# Run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
