import config
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
        command_type = parsed.get('type')
        intent = parsed.get('intent')
        
        if command_type == 'hardware_query':
            return self._handle_hardware_query(intent)
        elif command_type == 'help':
            return self._handle_help()
        else:
            return "I'm not sure how to help. Try asking for help."
    
    def _handle_hardware_query(self, intent):
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
            status = self.hardware.get_full_status()
            return f"CPU: {status['cpu_percent']:.1f}% | Memory: {status['memory_percent']:.1f}% | Disk: {status['disk_percent']:.1f}% | Temp: {status['temperature']}°C"
        return "Please specify which hardware to check."
    
    def _handle_help(self):
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
    
    def run_interactive(self):
        self.running = True
        while self.running:
            try:
                command = input("\nYou: ").strip()
                if not command:
                    continue
                if command.lower() in ['exit', 'quit']:
                    break
                response = self.process_command(command)
                print(f"\n🤖 Jarvis: {response}")
            except KeyboardInterrupt:
                break
        self.running = False
    
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
