FROM python:3.11-slim

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc && rm -rf /var/lib/apt/lists/*

# Create a non-root user 'appuser' with home directory /home/appuser
RUN useradd --create-home appuser

# Set workdir and copy files with ownership changed to appuser
WORKDIR /app

# Copy requirements first for caching
COPY --chown=appuser:appuser requirements.txt /app/

# Switch to appuser before installing packages
USER appuser

# Set HOME env so pip uses this dir, and adjust PATH for venv
ENV HOME=/home/appuser
ENV PATH="/app/venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create python virtual environment & install dependencies in one command layer
RUN python -m venv /app/venv && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all source code as appuser
COPY --chown=appuser:appuser . /app

# Expose port and run app
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
