import psutil
import time

start_time = time.time()

def get_status():
    uptime = time.time() - start_time
    return {
        "memory_used_mb": round(psutil.virtual_memory().used / (1024 * 1024), 2),
        "memory_total_mb": round(psutil.virtual_memory().total / (1024 * 1024), 2),
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "uptime_seconds": int(uptime)
    }