import pyttsx3
try:
    import speech_recognition as sr
except:
    sr = None

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        
        if sr:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
        else:
            self.recognizer = None
    
    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            print(f"Jarvis: {text}")
    
    def listen(self):
        if not self.recognizer:
            return None
        
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=10)
            return self.recognizer.recognize_google(audio)
        except:
            return None
