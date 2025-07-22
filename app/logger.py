import os
import json
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "log.jsonl")

os.makedirs(LOG_DIR, exist_ok=True)

def log_interaction(request_data, response_data):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "request": request_data,
        "response": response_data
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")