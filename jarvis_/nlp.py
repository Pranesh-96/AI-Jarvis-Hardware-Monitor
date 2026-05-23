import re
import config

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
