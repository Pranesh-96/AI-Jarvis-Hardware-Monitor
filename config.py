# ✅ ALL FEATURES ENABLED
FEATURES = {
    'voice_control': True,
    'text_commands': True,
    'nlp_enabled': True,
    'hardware_monitoring': True,
    'temperature_monitoring': True,
    'scheduling': True,
    'automation': True,
    'alerts': True,
}

# ✅ ALL PERMISSIONS GRANTED
PERMISSIONS = {
    'read_cpu': True,
    'read_memory': True,
    'read_disk': True,
    'read_temperature': True,
    'read_battery': True,
    'access_microphone': True,
    'access_speaker': True,
}

# Hardware thresholds
HARDWARE = {
    'cpu_threshold_high': 80,
    'cpu_threshold_medium': 50,
    'memory_threshold_high': 80,
    'memory_threshold_medium': 50,
    'disk_threshold_high': 85,
    'disk_threshold_medium': 60,
    'temp_threshold_high': 80,
    'temp_threshold_medium': 60,
    'temp_threshold_critical': 95,
    'monitoring_interval': 2,
}

# Voice settings
VOICE = {
    'engine': 'pyttsx3',
    'voice_rate': 150,
    'voice_volume': 1.0,
    'language': 'en',
    'auto_respond': True,
    'listen_continuously': True,
    'timeout': 10,
}

# NLP settings
NLP = {
    'enable_all_commands': True,
    'fuzzy_matching': True,
}

# Monitoring settings
MONITORING = {
    'auto_start': True,
    'continuous_monitoring': True,
    'background_mode': True,
}

# Auto-startup
AUTO_STARTUP = {
    'enable_auto_launch': True,
    'start_on_boot': True,
    'background_on_launch': True,
}
