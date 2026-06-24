import socket
import platform
from datetime import datetime

hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
finally:
    s.close()

print("=" * 40)
print("SYSTEM INFORMATION")
print("=" * 40)

print("Host Name :", hostname)
print("IP Address:", ip)
print("OS        :", platform.system())
print("Release   :", platform.release())
print("Date/Time :", datetime.now())

print("=" * 40)
