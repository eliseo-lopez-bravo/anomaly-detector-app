# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user and group, with UID and GID 1001
RUN groupadd -r appgroup -g 1001 && \
    useradd -r -u 1001 -g appgroup -m -d /home/appuser -s /bin/bash appuser

# Give ownership of /app to the non-root user
RUN chown -R appuser:appgroup /app

# Set environment variables for non-root user
ENV HOME=/home/appuser
ENV USER=appuser
ENV PATH="/app/venv/bin:${PATH}"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Switch to non-root user
USER appuser

# Create virtual environment in /app/venv as appuser
RUN python -m venv /app/venv

# Copy requirements and install packages inside venv
COPY --chown=appuser:appgroup requirements.txt .
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy app code owned by appuser
COPY --chown=appuser:appgroup . .

# Expose port
EXPOSE 8080

# Command to run the app using uvicorn from venv
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
