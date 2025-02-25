#!/bin/bash

# Install FFmpeg with full codec support
apt-get update && \
apt-get install -y \
    ffmpeg \
    libavcodec-extra \
    libavfilter-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*
