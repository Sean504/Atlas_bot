import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import time
import requests
import st7789
from PIL import Image, ImageDraw
import os
from difflib import SequenceMatcher
import numpy as np
import re

class Tool:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func

def calculator(expression):
    try:
        cleaned = re.sub(r'[^0-9\+\-\*\/\(\)\.\s]', '', expression)
        safe_dict = {"__builtins__": None}
        return str(eval(cleaned, safe_dict))
    except:
        return "Error evaluating expression"

def datetime_tool():
    return time.strftime('%Y-%m-%d %H:%M:%S')

def execute_command(command):
    try:
        result = os.popen(command).read()
        return result if result else "Command executed successfully"
    except Exception as e:
        return f"Error executing command: {str(e)}"

def generate_code(description, code_type="python"):
   try:
       if not hasattr(self, 'selected_model'):
           return "Error: No model selected"
           
       prompt = "Write code for: " + description + "\nRequirements:\n- Production quality\n- Error handling\n- Comments\n- No explanations, just code"
       
       payload = {
           "model": self.selected_model,
           "prompt": prompt,
           "stream": False,
           "raw": True
       }
       
       response = requests.post("http://127.0.0.1:11434/api/generate", json=payload)
       
       if response.status_code != 200:
           return f"Error: API returned status {response.status_code}"
           
       result = response.json()
       code = result['response']
       
       ext = {'python': '.py', 'javascript': '.js', 'html': '.html'}[code_type]
       filename = f"script_{int(time.time())}{ext}"
       
       with open(filename, 'w') as f:
           f.write(code.strip())
           
       return f"Generated {code_type} script saved as {filename}"
       
   except Exception as e:
       return f"Error generating code: {str(e)}"
def run_python_script(filename):
    try:
        if not filename.endswith('.py'):
            filename += '.py'
        result = os.popen(f'python {filename}').read()
        return result if result else "Script executed successfully"
    except Exception as e:
        return f"Error executing Python script: {str(e)}"

def write_document(text, filename=None):
    try:
        if not filename:
            filename = f"doc_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(text)
        return f"Document saved as {filename}"
    except Exception as e:
        return f"Error writing document: {str(e)}"

def read_document(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading document: {str(e)}"

def list_directory(path="."):
    try:
        return "\n".join(os.listdir(path))
    except Exception as e:
        return f"Error listing directory: {str(e)}"

class VoiceDetector:
    def __init__(self):
        self.model = Model("model")
        self.q = queue.Queue(maxsize=1024)
        devices = sd.query_devices()
        print("\nAvailable audio devices:")
        for i, dev in enumerate(devices):
            print(f"{i}: {dev['name']}")
        self.device = 0
        device_info = sd.query_devices(self.device, 'input')
        print(f"\nUsing device: {device_info['name']}")
        self.samplerate = int(device_info['default_samplerate'])
        self.channels = 1
        self.blocksize = 4096
        self.buffer_duration = 0.5
        self.audio_buffer = []
        self.buffer_max_size = int(self.samplerate * self.buffer_duration)
        self.confidence_threshold = 0.3
        self.listening_for_wake = True
        self.ollama_url = "http://127.0.0.1:11434"
        self.selected_model = self.select_model()
        self.last_speech_time = time.time()
        self.speech_timeout = 3.0
        self.accumulated_text = []
        
        self.tools = {
            'calculator': Tool('calculator', 'Evaluate math expressions', calculator),
            'datetime': Tool('datetime', 'Get current date and time', datetime_tool),
            'terminal': Tool('terminal', 'Execute terminal commands', execute_command),
            'write': Tool('write', 'Write text to document', write_document),
            'read': Tool('read', 'Read document content', read_document),
            'ls': Tool('ls', 'List directory contents', list_directory),
            'generate_python': Tool('generate_python', 'Generate Python script', lambda x: generate_code(x, 'python')),
            'generate_javascript': Tool('generate_javascript', 'Generate JavaScript code', lambda x: generate_code(x, 'javascript')),
            'generate_html': Tool('generate_html', 'Generate HTML code', lambda x: generate_code(x, 'html')),
            'run_python': Tool('run_python', 'Execute Python script', run_python_script)
        }

        self.display = st7789.ST7789(
            height=240,
            width=240,
            rotation=90,
            port=0,
            cs=1,
            dc=9,
            backlight=13,
            spi_speed_hz=80 * 1000 * 1000,
            offset_left=0,
            offset_top=0
        )
        self.display.begin()
        self.set_display_black()

        print("Testing audio output...")
        self.speak("Atlas is ready")

        self.wake_phrases = [
            "hey atlas",
            "hi atlas", 
            "hello atlas",
            "okay atlas",
            "yo atlas",
            "atlas",
            "listen atlas",
            "excuse me atlas",
            "hey alice",
            "hey at last",
            "hay atlas",
            "hey add less",
            "hey alice",
            "hey atlus",
            "a atlas",
            "hey atlas",
            "hey addless",
            "atlas",
            "at last",
            "atlas",
            "adalus",
            "adalis"
        ]

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def check_wake_word(self, text):
        words = text.lower().split()
        
        for phrase in self.wake_phrases:
            if phrase in text:
                return True, 1.0

        max_score = 0
        for i in range(len(words) - 1):
            test_phrase = ' '.join(words[i:i+2])
            for phrase in self.wake_phrases:
                score = self.similar(test_phrase, phrase)
                max_score = max(max_score, score)
                if score > 0.8:
                    return True, score

        for word in words:
            if "atlas" in word and len(word) >= 4:
                return True, 0.9
            for phrase in self.wake_phrases:
                if self.similar(word, phrase) > 0.85:
                    return True, 0.85

        return False, max_score

    def speak(self, text):
        try:
            os.system(f'flite -voice slt -t "{text}"')
        except Exception as e:
            print(f"Speech error: {str(e)}")

    def set_display_mint(self):
        image = Image.new('RGB', (240, 240), (152, 255, 152))
        self.display.display(image)

    def set_display_black(self):
        image = Image.new('RGB', (240, 240), (0, 0, 0))
        self.display.display(image)

    def process_tool_commands(self, text):
        text = text.lower()
        if "calculate" in text:
            expression = text.replace("calculate", "").strip()
            return self.tools['calculator'].func(expression)
        elif "time" in text or "date" in text:
            return self.tools['datetime'].func()
        elif text.startswith("run") or text.startswith("execute"):
            if "python" in text:
                script = text.replace("run", "").replace("python", "").strip()
                return self.tools['run_python'].func(script)
            command = text.replace("run", "").replace("execute", "").strip()
            return self.tools['terminal'].func(command)
        elif "generate" in text or "create" in text:
            if "python" in text:
                desc = text.replace("generate", "").replace("create", "").replace("python", "", 1).strip()
                return self.tools['generate_python'].func(desc)
            elif "javascript" in text or "js" in text:
                desc = text.replace("generate", "").replace("create", "").replace("javascript", "").replace("js", "").strip()
                return self.tools['generate_javascript'].func(desc)
            elif "html" in text:
                desc = text.replace("generate", "").replace("create", "").replace("html", "", 1).strip()
                return self.tools['generate_html'].func(desc)
        elif text.startswith("write") or text.startswith("right"):
            content = text.replace("write", "").replace("right", "").strip()
            return self.tools['write'].func(content)
        elif text.startswith("read"):
            filename = text.replace("read", "", 1).strip()
            return self.tools['read'].func(filename)
        elif "list files" in text or "show files" in text:
            return self.tools['ls'].func()
        return None

    def get_available_models(self):
        try:
            response = requests.get(f"{self.ollama_url}/api/tags")
            if response.status_code == 200:
                models = response.json().get('models', [])
                return [model['name'] for model in models]
            return []
        except Exception as e:
            print(f"Error getting models: {str(e)}")
            return []

    def select_model(self):
        print("\nGetting available models...")
        models = self.get_available_models()
        
        if not models:
            print("No models found, using default: smollm:135m")
            return "smollm:135m"
        
        print("\nAvailable models:")
        for i, model in enumerate(models):
            print(f"{i}: {model}")
        
        while True:
            try:
                choice = input("\nSelect model number: ")
                index = int(choice)
                if 0 <= index < len(models):
                    selected = models[index]
                    print(f"\nSelected model: {selected}")
                    return selected
                print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def audio_callback(self, indata, frames, time, status):
        try:
            data = np.frombuffer(indata, dtype=np.int16)
            amplified_data = (data * 1.5).astype(np.int16)
            if not self.q.full():
                self.q.put_nowait(bytes(amplified_data))
        except queue.Full:
            with self.q.mutex:
                self.q.queue.clear()
  
    def get_ollama_response(self, user_text):
        try:
            if any(word in user_text.lower() for word in ['generate', 'create']) and 'python' in user_text.lower():
                return self.tools['generate_python'].func(user_text)
            elif any(word in user_text.lower() for word in ['generate', 'create']) and ('javascript' in user_text.lower() or 'js' in user_text.lower()):
                return self.tools['generate_javascript'].func(user_text)
            elif any(word in user_text.lower() for word in ['generate', 'create']) and 'html' in user_text.lower():
                return self.tools['generate_html'].func(user_text)
           
            tool_result = self.process_tool_commands(user_text)
            if tool_result:
                self.speak(tool_result)
                return tool_result

            prompt = "You are a concise AI assistant. Only respond in 3 sentences maximum. Here is the user's message: " + user_text
            payload = {
                "model": self.selected_model,
                "prompt": prompt,
                "stream": True
             }
            print("Sending message to Atlas...")
            response = requests.post(f"{self.ollama_url}/api/generate", json=payload, timeout=60, stream=True)
       
            if response.status_code == 200:
                full_response = ""
                print("Atlas is thinking...")
                for line in response.iter_lines():
                    if line:
                        json_response = json.loads(line)
                        if 'response' in json_response:
                            full_response += json_response['response']
                        if json_response.get('done', False):
                            break
                print("Atlas has responded.")
                self.speak(full_response)
                return full_response
            else:
                print(f"Error response: {response.text}")
                return f"Error: Status code {response.status_code}"
        except requests.exceptions.Timeout:
            return "Error: Request timed out"
        except Exception as e:
            print(f"Exception in message to Atlas: {str(e)}")
            return f"Error: {str(e)}"

    def run(self):
        try:
            print("\nStarting voice detection...")
            with sd.RawInputStream(
                samplerate=self.samplerate,
                blocksize=self.blocksize,
                device=self.device,
                dtype='int16',
                channels=self.channels,
                callback=self.audio_callback
            ) as stream:
                print("\nWaiting for wake words...")
                rec = KaldiRecognizer(self.model, self.samplerate)
                
                while True:
                    try:
                        data = self.q.get(timeout=0.1)
                        if rec.AcceptWaveform(data):
                            result = json.loads(rec.Result())
                            text = result.get("text", "").lower()
                            base_confidence = float(result.get("confidence", 0))
                            
                            if text:
                                if self.listening_for_wake:
                                    is_wake_word, wake_score = self.check_wake_word(text)
                                    combined_confidence = (base_confidence + wake_score) / 2
                                    
                                    if is_wake_word and combined_confidence > self.confidence_threshold:
                                        print(f"Wake word detected [Confidence: {combined_confidence:.2f}]")
                                        print("I'm listening...")
                                        self.set_display_mint()
                                        self.listening_for_wake = False
                                        with self.q.mutex:
                                            self.q.queue.clear()
                                    elif wake_score > 0.6:
                                        print(f"Possible wake word detected: '{text}' [Score: {wake_score:.2f}]")
                                
                                elif not self.listening_for_wake:
                                      if text:
                                          self.accumulated_text.append(text)
                                          print("Current input:", text)
    
                                      current_time = time.time()
                                      listen_duration = current_time - self.last_speech_time
    
                                      if listen_duration >= 3.0:
                                        if self.accumulated_text:
                                            full_text = " ".join(self.accumulated_text)
                                            print("\nProcessing command:", full_text)
                                            response = self.get_ollama_response(full_text)
                                            print("\nAtlas:", response)
                                            with open('voice_log.txt', 'a') as f:
                                                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} user: {full_text}\n")
                                                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} atlas: {response}\n")
                                            self.accumulated_text = []
                                            self.listening_for_wake = True
                                            self.set_display_black()
                                            print("\nWaiting for wake words...")
                    except queue.Empty:
                        continue
        except KeyboardInterrupt:
            print("\nStopping...")
            self.set_display_black()
        except Exception as e:
            print(f"Error: {e}")
            self.set_display_black()

if __name__ == "__main__":
    detector = VoiceDetector()
    detector.run()
