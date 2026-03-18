from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)

def log(message):
    with open("logs/activity.log", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")
