#!/usr/bin/env python3
# ============================================================================
# AI JARVIS - MAIN ENTRY POINT
# ============================================================================

import os
import sys
import time
import threading
from datetime import datetime

try:
    from jarvis.core import JarvisAI
    from jarvis.hardware import HardwareMonitor
    import config
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Please install required packages: pip install -r requirements.txt")
    sys.exit(1)

class JarvisLauncher:
    def __init__(self):
        self.jarvis = None
        self.hardware = None
        self.running = False
        self.monitoring_thread = None
        
    def initialize_jarvis(self):
        print("\n" + "="*70)
        print("🤖 INITIALIZING AI JARVIS - HARDWARE MONITOR")
        print("="*70)
        
        try:
            print("\n🔌 Initializing AI Core...")
            self.jarvis = JarvisAI()
            print("   ✅ AI Core: READY")
            
            print("📊 Initializing Hardware Monitor...")
            self.hardware = HardwareMonitor()
            print("   ✅ Hardware Monitor: READY")
            
            self.display_startup_info()
            
            print("\n" + "="*70)
            print("🎉 JARVIS IS NOW FULLY OPERATIONAL")
            print("="*70)
            
            return True
            
        except Exception as e:
            print(f"\n❌ Initialization Error: {e}")
            return False
    
    def display_startup_info(self):
        print("\n" + "-"*70)
        print("📋 ACTIVE CONFIGURATIONS:")
        print("-"*70)
        
        features = [
            ("Voice Control", True),
            ("Text Commands", True),
            ("NLP Processing", True),
            ("Hardware Monitoring", True),
            ("Temperature Monitoring", True),
            ("Task Scheduling", True),
            ("Auto-Startup", True),
        ]
        
        for feature, status in features:
            status_symbol = "✅" if status else "❌"
            print(f"  {status_symbol} {feature}: {'ENABLED' if status else 'DISABLED'}")
        
        print("-"*70)
    
    def run_interactive_mode(self):
        print("\n" + "="*70)
        print("💬 INTERACTIVE MODE")
        print("="*70)
        print("\n📝 Example Commands:")
        print("   • 'What is my CPU usage?'")
        print("   • 'Check my temperature'")
        print("   • 'System status'")
        print("   • 'help'")
        print("   • 'exit'\n")
        
        self.jarvis.run_interactive()
    
    def start(self, mode='interactive'):
        if not self.initialize_jarvis():
            return
        
        self.running = True
        
        try:
            if mode.lower() == 'voice':
                print("\n🎤 VOICE MODE - Listening for commands...")
                self.jarvis.run_voice_mode()
            elif mode.lower() == 'monitoring':
                print("\n📊 CONTINUOUS MONITORING MODE")
                self.run_monitoring_mode()
            else:
                self.run_interactive_mode()
        
        except KeyboardInterrupt:
            print("\n\n🛑 Shutting down Jarvis...")
        finally:
            self.running = False
            print("\n👋 Goodbye!\n")

    def run_monitoring_mode(self):
        print("Real-time system monitoring active...\n")
        try:
            while self.running:
                status = self.hardware.get_full_status()
                print(f"\n[{datetime.now().strftime('%H:%M:%S')}] System Status:")
                print(f"  CPU: {status.get('cpu_percent', 0):.1f}% ({status.get('cpu_status', 'N/A')})")
                print(f"  Memory: {status.get('memory_percent', 0):.1f}% ({status.get('memory_status', 'N/A')})")
                print(f"  Disk: {status.get('disk_percent', 0):.1f}% ({status.get('disk_status', 'N/A')})")
                print(f"  Temperature: {status.get('temperature', 'N/A')}°C ({status.get('temp_status', 'N/A')})")
                print(f"  Overall: {status.get('status', 'UNKNOWN')}")
                time.sleep(2)
        except KeyboardInterrupt:
            pass

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='🤖 AI Jarvis - Hardware Monitor')
    parser.add_argument('--voice', action='store_true', help='Voice control mode')
    parser.add_argument('--monitor', action='store_true', help='Monitoring mode')
    
    args = parser.parse_args()
    
    mode = 'voice' if args.voice else 'monitoring' if args.monitor else 'interactive'
    
    launcher = JarvisLauncher()
    launcher.start(mode=mode)

if __name__ == '__main__':
    main()
