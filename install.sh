#!/bin/bash


# Install system dependencies
sudo apt-get update
sudo apt-get install python3.10-venv
sudo apt-get install -y \

   python3-pip \
   python3-dev \
   portaudio19-dev \
   python3-pyaudio \
   flite \
   flite1-dev \
   libsndfile1 \
   libsndfile1-dev \
   spi-tools \
   libatlas-base-dev

# Python packages
pip install \
   vosk \
   sounddevice \
   soundfile \
   numpy \
   requests \
   Pillow \
   spidev \
   st7789
# Create Python virtual environment
python3 -m venv atlas_env
source atlas_env/bin/activate

# Download Vosk model
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
mv vosk-model-small-en-us-0.15 model

# Install Ollama
curl https://ollama.ai/install.sh | sh

# Pull Smollm models
ollama pull smollm2:1.7b
ollama pull smollm2:360m
ollama pull smollm:360m

# Enable SPI if on Raspberry Pi
if [ -f /usr/bin/raspi-config ]; then
   sudo raspi-config nonint do_spi 0
fi

# Set audio permissions
sudo usermod -a -G audio $USER
sudo usermod -a -G spi $USER

echo "Installation complete. Run 'source atlas_env/bin/activate' to start."
