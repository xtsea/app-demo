FROM python:3.11-slim

WORKDIR /app

RUN apt -qq update && \
    apt -qq install -y --no-install-recommends \
    ffmpeg \
    curl \
    git \
    gnupg2 \
    unzip \
    wget \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libappindicator3-1 \
    libxrender1 \
    libxtst6 \
    libnss3 \
    libatk1.0-0 \
    libxss1 \
    fonts-liberation \
    libasound2 \
    libgbm-dev \
    libu2f-udev \
    libvulkan1 \
    libgl1-mesa-dri \
    xdg-utils \
    python3-dev \
    python3-pip \
    libavformat-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavfilter-dev \
    libavutil-dev \
    libswscale-dev \
    libswresample-dev \
    neofetch && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/

COPY requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
