import psutil
import config

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
        status = self._classify_status(percent, config.HARDWARE['cpu_threshold_high'], config.HARDWARE['cpu_threshold_medium'])
        return {'percent': percent, 'status': status}
    
    def get_memory_status(self):
        memory = psutil.virtual_memory()
        status = self._classify_status(memory.percent, config.HARDWARE['memory_threshold_high'], config.HARDWARE['memory_threshold_medium'])
        return {'percent': memory.percent, 'status': status}
    
    def get_disk_status(self):
        disk = psutil.disk_usage('/')
        status = self._classify_status(disk.percent, config.HARDWARE['disk_threshold_high'], config.HARDWARE['disk_threshold_medium'])
        return {'percent': disk.percent, 'status': status}
    
    def get_temperature_status(self):
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                cpu_temp = list(temps.values())[0][0].current if temps else 50
            else:
                cpu_temp = 50
        except:
            cpu_temp = 50
        
        if cpu_temp >= config.HARDWARE['temp_threshold_critical']:
            status = 'CRITICAL'
        elif cpu_temp >= config.HARDWARE['temp_threshold_high']:
            status = 'HIGH'
        elif cpu_temp >= config.HARDWARE['temp_threshold_medium']:
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
