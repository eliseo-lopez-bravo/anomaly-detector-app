FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc && rm -rf /var/lib/apt/lists/*

# Create non-root user with home directory
RUN useradd --create-home appuser

# Set working directory and give ownership to appuser
WORKDIR /app
RUN chown appuser:appuser /app

# Switch to non-root user
USER appuser

# Set environment variables for python and home
ENV HOME=/home/appuser
ENV PATH="/app/venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create virtual environment
RUN python -m venv /app/venv

# Copy requirements and install packages in one RUN step to keep env
COPY --chown=appuser:appuser requirements.txt /app/
RUN /app/venv/bin/pip install --upgrade pip && /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=appuser:appuser . /app

# Expose port and run
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
