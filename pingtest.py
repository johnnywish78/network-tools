import subprocess

host = input("Target: ")
count = input("How many pings? ")

result = subprocess.run(
    ["ping", "-c", count, host],
    capture_output=True,
    text=True
)

print(result.stdout)
