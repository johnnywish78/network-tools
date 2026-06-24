import socket
import platform
from datetime import datetime
import subprocess

print("=" * 50)
print("NETDOCTOR v1.0")
print("=" * 50)

# Hostname
hostname = socket.gethostname()
print("Host Name :", hostname)

# Local IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
finally:
    s.close()

print("Local IP  :", ip)

# OS Info
print("OS        :", platform.system())
print("Release   :", platform.release())

# Date & Time
print("Date/Time :", datetime.now())

print("-" * 50)

# Internet Test
result = subprocess.run(
    ["ping", "-c", "2", "1.1.1.1"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Internet  : ONLINE")
else:
    print("Internet  : OFFLINE")

print("=" * 50)
