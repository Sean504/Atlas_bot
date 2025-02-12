Atlas Voice Assistant 🎙️
A locally-running voice-controlled AI assistant using Ollama and Vosk.
Show Image
🚀 Quick Start
bashCopychmod +x install.sh
./install.sh
source atlas_env/bin/activate
python atlas.py
🎯 Features

🗣️ Voice Activation ("Hey Atlas")
🤖 Local AI Processing (No cloud dependency)
💻 Code Generation
🧮 Calculator
📁 File Operations
⌚ System Tools
📊 Visual Feedback (ST7789 Display)

🎤 Voice Commands
CategoryCommandsDescriptionCode Generation"generate python script for..."Creates Python scripts"create javascript for..."Generates JavaScript code"make html for..."Creates HTML filesMath"calculate 2 + 2"Basic arithmeticFiles"write [text] to file"Creates text files"read [filename]"Reads file content"list files"Shows directory contentsSystem"what's the time?"Current time/date"run [command]"Executes system commands
🔧 Technical Details
Core Components
pythonCopyclass VoiceDetector:
    def __init__(self):
        # Initialize models
        self.model = Model("model")  # Vosk
        self.selected_model = self.select_model()  # Ollama
        
        # Setup audio
        self.samplerate = int(device_info['default_samplerate'])
        self.channels = 1
        self.blocksize = 4096
Tools System
pythonCopyclass Tool:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func

tools = {
    'calculator': Tool('calculator', 'Math operations', calculator),
    'datetime': Tool('datetime', 'Time/date info', datetime_tool),
    'generate_python': Tool('generate_python', 'Create Python code', generate_code)
    # ... more tools
}
🛠️ Installation Details
Prerequisites

Python 3.x
Raspberry Pi (recommended)
USB Microphone
Speaker
ST7789 Display (optional)

System Dependencies
bashCopysudo apt-get install -y
    python3-pip
    python3-dev
    portaudio19-dev
    python3-pyaudio
    flite
    flite1-dev
AI Models

Vosk (Speech Recognition)
Smollm Models:

smollm2:1.7b
smollm2:360m
smollm:360m



🌟 Key Features Explained
Speech Recognition

Wake word detection
Fuzzy matching for commands
Confidence scoring

Code Generation

Python script generation
JavaScript/HTML creation
Error handling included

Tool System

Modular design
Easy to extend
Command parsing

📝 Contributing

Fork the repository
Create feature branch
Commit changes
Push to branch
Open pull request

🔍 Troubleshooting
Common issues and solutions:

Microphone not detected: Check arecord -l
Models not loading: Verify Ollama service
Display issues: Check SPI configuration

📄 License
MIT License - free to use and modify
🙏 Acknowledgments

Vosk for speech recognition
Ollama team for local AI
SmolLM developers

🔗 Contact
Open an issue for bugs or suggestions
