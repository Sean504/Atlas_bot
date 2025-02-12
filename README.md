Atlas Voice Assistant
A voice-controlled AI assistant that runs locally using Ollama and Vosk for speech recognition.
Installation

Run install script:

bashCopychmod +x install.sh
./install.sh

Activate environment:

bashCopysource atlas_env/bin/activate
Features

Voice activation ("Hey Atlas")
Local AI processing using Smollm models
Code generation for Python, JavaScript, HTML
Calculator functions
File operations (read/write)
System commands
Date/time queries
Directory listing

Voice Commands

"Hey Atlas, generate python script for [description]"
"Hey Atlas, calculate [expression]"
"Hey Atlas, write [text] to file"
"Hey Atlas, read [filename]"
"Hey Atlas, list files"
"Hey Atlas, what's the time?"
"Hey Atlas, run [command]"

Hardware Requirements

Microphone (USB/Built-in)
Speaker
ST7789 Display (optional)
Raspberry Pi (recommended)

Models
Uses local models:

smollm2:1.7b
smollm2:360m
smollm:360m
Vosk speech recognition

Troubleshooting

Ensure microphone permissions
Check Ollama service is running
Verify audio device selection

Requirements
Listed in install.sh:

Python 3.x
Vosk
SoundDevice
Ollama
Various system dependencies
