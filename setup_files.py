import os

# Create jarvis folder
os.makedirs('jarvis', exist_ok=True)

# Create __init__.py
with open('jarvis/__init__.py', 'w') as f:
    f.write('''__version__ = "1.0.0"
__author__ = "Pranesh-96"
''')
    print("✅ Created jarvis/__init__.py")

# Create hardware.py
with open('jarvis/hardware.py', 'w') as f:
    f.write('''import psutil

class HardwareMonitor:
    def __init__(self):
        pass
    
    def _classify_status(self, percent, high, medium):
        if percent >= high:
            return 'HIGH'
        elif percent >= medium:
            return 'MEDIUM'
        else:
            return 'LOW'
    
    def get_cpu_status(self):
        percent = psutil.cpu_percent(interval=1)
        return {'percent': percent, 'status': self._classify_status(percent, 80, 50)}
    
    def get_memory_status(self):
        memory = psutil.virtual_memory()
        return {'percent': memory.percent, 'status': self._classify_status(memory.percent, 80, 50)}
    
    def get_disk_status(self):
        disk = psutil.disk_usage('/')
        return {'percent': disk.percent, 'status': self._classify_status(disk.percent, 85, 60)}
    
    def get_temperature_status(self):
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                cpu_temp = list(temps.values())[0][0].current
            else:
                cpu_temp = 50
        except:
            cpu_temp = 50
        
        if cpu_temp >= 95:
            status = 'CRITICAL'
        elif cpu_temp >= 80:
            status = 'HIGH'
        elif cpu_temp >= 60:
            status = 'MEDIUM'
        else:
            status = 'LOW'
        
        return {'temperature': cpu_temp, 'status': status}
    
    def get_full_status(self):
        cpu = self.get_cpu_status()
        memory = self.get_memory_status()
        disk = self.get_disk_status()
        temp = self.get_temperature_status()
        
        return {
            'cpu_percent': cpu['percent'],
            'cpu_status': cpu['status'],
            'memory_percent': memory['percent'],
            'memory_status': memory['status'],
            'disk_percent': disk['percent'],
            'disk_status': disk['status'],
            'temperature': temp['temperature'],
            'temp_status': temp['status'],
            'status': 'HEALTHY'
        }
''')
    print("✅ Created jarvis/hardware.py")

# Create voice.py
with open('jarvis/voice.py', 'w') as f:
    f.write('''import pyttsx3
try:
    import speech_recognition as sr
except:
    sr = None

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        if sr:
            self.recognizer = sr.Recognizer()
            try:
                self.microphone = sr.Microphone()
            except:
                self.microphone = None
        else:
            self.recognizer = None
    
    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            print(f"🤖 Jarvis: {text}")
    
    def listen(self):
        if not self.recognizer or not self.microphone:
            return None
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=10)
            return self.recognizer.recognize_google(audio)
        except:
            return None
''')
    print("✅ Created jarvis/voice.py")

# Create nlp.py
with open('jarvis/nlp.py', 'w') as f:
    f.write('''import re

class CommandProcessor:
    def __init__(self):
        self.patterns = {
            'cpu': [r'cpu', r'processor'],
            'memory': [r'memory', r'ram'],
            'disk': [r'disk', r'storage'],
            'temperature': [r'temperature', r'temp', r'heat'],
            'full_report': [r'full', r'report', r'all'],
        }
    
    def parse_command(self, command):
        command_lower = command.lower()
        
        for intent, patterns in self.patterns.items():
            for pattern in patterns:
                if pattern in command_lower:
                    return {'type': 'hardware_query', 'intent': intent}
        
        if 'help' in command_lower:
            return {'type': 'help', 'intent': 'general'}
        
        if 'exit' in command_lower or 'quit' in command_lower:
            return {'type': 'exit', 'intent': 'exit'}
        
        return {'type': 'unknown', 'intent': 'unknown'}
''')
    print("✅ Created jarvis/nlp.py")

# Create scheduler.py
with open('jarvis/scheduler.py', 'w') as f:
    f.write('''class TaskScheduler:
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task_id, func):
        self.tasks[task_id] = func
''')
    print("✅ Created jarvis/scheduler.py")

# Create core.py
with open('jarvis/core.py', 'w') as f:
    f.write('''import config
from jarvis.hardware import HardwareMonitor
from jarvis.voice import VoiceAssistant
from jarvis.nlp import CommandProcessor

class JarvisAI:
    def __init__(self):
        self.hardware = HardwareMonitor()
        self.voice = VoiceAssistant()
        self.nlp = CommandProcessor()
        self.running = False
    
    def process_command(self, command):
        parsed = self.nlp.parse_command(command)
        intent = parsed.get('intent')
        
        if parsed['type'] == 'hardware_query':
            if 'cpu' in intent:
                status = self.hardware.get_cpu_status()
                return f"CPU Usage: {status['percent']:.1f}% - Status: {status['status']}"
            elif 'memory' in intent:
                status = self.hardware.get_memory_status()
                return f"Memory Usage: {status['percent']:.1f}% - Status: {status['status']}"
            elif 'disk' in intent:
                status = self.hardware.get_disk_status()
                return f"Disk Usage: {status['percent']:.1f}% - Status: {status['status']}"
            elif 'temperature' in intent:
                status = self.hardware.get_temperature_status()
                return f"System Temperature: {status['temperature']}°C - Status: {status['status']}"
            elif 'full' in intent:
                s = self.hardware.get_full_status()
                return f"CPU: {s['cpu_percent']:.1f}% ({s['cpu_status']}) | Memory: {s['memory_percent']:.1f}% ({s['memory_status']}) | Disk: {s['disk_percent']:.1f}% ({s['disk_status']}) | Temp: {s['temperature']}°C ({s['temp_status']})"
        elif parsed['type'] == 'help':
            return """
🤖 JARVIS - AI HARDWARE MONITOR

Commands:
• "What is my CPU usage?"
• "Check my temperature"
• "Memory usage"
• "Disk status"
• "Full system report"
• "help"
• "exit"
            """
        return "I didn't understand. Try 'help'"
    
    def run_interactive(self):
        self.running = True
        print("\\n" + "-"*70)
        print("💬 INTERACTIVE MODE")
        print("-"*70)
        print("Type your commands (or 'help' for commands)\\n")
        
        while self.running:
            try:
                command = input("You: ").strip()
                if not command:
                    continue
                if command.lower() in ['exit', 'quit']:
                    break
                response = self.process_command(command)
                print(f"\\n🤖 Jarvis: {response}\\n")
            except KeyboardInterrupt:
                break
        self.running = False
        print("\\n👋 Goodbye!\\n")
    
    def run_voice_mode(self):
        self.running = True
        self.voice.speak("Hello! I'm Jarvis. Say your command now.")
        while self.running:
            command = self.voice.listen()
            if not command:
                continue
            if command.lower() in ['exit', 'quit', 'bye']:
                self.voice.speak("Goodbye!")
                break
            response = self.process_command(command)
            self.voice.speak(response)
        self.running = False
''')
    print("✅ Created jarvis/core.py")

print("\n" + "="*70)
print("✅ ALL JARVIS FILES CREATED SUCCESSFULLY!")
print("="*70)
print("\nNow run: python main.py")
