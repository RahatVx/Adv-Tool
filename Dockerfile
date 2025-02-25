FROM python:3.11-slim-bullseye

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1-mesa-glx \
    ghostscript \
    imagemagick \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create storage directories
RUN mkdir -p /app/storage/{temp,uploads,processed}

VOLUME /app/storage

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "bot.web.routes:app"]
