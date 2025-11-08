import psutil
from email_automation import send_email

def monitor_system():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if cpu > 80 or memory > 80 or disk > 90:
        send_email(
            "System Alert",
            f"CPU: {cpu}%  Memory: {memory}%  Disk: {disk}%",
            "your_email@example.com")