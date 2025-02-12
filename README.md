# Atlas AI Assistant 🤖

> Local voice & text AI assistant powered by Ollama and Vosk

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

### 🎯 Core Features
- 🗣️ Voice & text interaction modes
- 🤖 Local AI processing (no cloud required)
- 💻 Code generation (Python, JS, HTML)
- 🔧 System tools & file operations
- 📊 Visual feedback via ST7789 display

### 🛠️ Technical Features
- 🎤 Wake word detection with fuzzy matching
- 🔊 Multi-device audio support
- 🧠 Ollama model selection
- 📝 Conversation logging
- ⚡ Real-time command processing

## ⚙️ Installation

### 📋 Prerequisites
- 🖥️ Raspberry Pi/Linux system
- 🐍 Python 3.8+
- 🎤 Microphone (voice mode)
- 🔊 Speaker (voice mode)
- 📺 ST7789 display (optional)

### 📥 Quick Install
```bash
git clone https://github.com/Sean504/Atlas-bot
cd Atlas-bot
chmod +x install.sh
./install.sh
source atlas_env/bin/activate
🔌 Hardware Setup
bashCopy# Audio Devices
arecord -l   # List inputs
aplay -l     # List outputs

# Display (ST7789)
VCC → 3.3V
GND → Ground
DIN → MOSI
CLK → SCLK
CS  → CE0
DC  → GPIO9
RST → GPIO25
BL  → GPIO13
📱 Usage
🚀 Getting Started

Launch Atlas: python atlas.py
Select mode:
1: Voice Input 🎤
2: Terminal Input ⌨️

Choose AI model:
CopyAvailable models:
0: smollm2:1.7b


Configure audio devices (voice mode)

💬 Commands
🗣️ Voice Mode

Wake word: "Hey Atlas"
Wait for green display
Speak command
3-second pause triggers processing

⌨️ Terminal Mode
bashCopyAtlas Terminal Mode
Type 'exit' to quit

You: generate python calculator
📝 Available Commands
TypeCommandExample💻 Codegenerate/create"generate python calculator"📁 Fileswrite/read"write hello to file.txt"🔧 Systemrun/execute"run ls -la"🧮 Mathcalculate"calculate 2 + 2"⏰ Timetime/date"what's the time?"
🔧 Troubleshooting

🎤 Audio Issues

bashCopy# Check devices

arecord -l
aplay -l

# Test recording

arecord -d 5 test.wav
aplay test.wav

# Permissions

groups | grep audio
sudo usermod -a -G audio $USER

🤖 Model Issues

bashCopy# Check Ollama
ollama list
ls ~/.ollama/models

# Reinstall models

ollama pull smollm2:360m

📺 Display Issues

bashCopy# Enable SPI
sudo raspi-config

# Check module

lsmod | grep spi
📚 Resources




Made with ❤️ using Ollama & Vosk
