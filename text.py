import time
import os

text = "HELLO GITHUB"

while True:
    os.system("clear")

    for i in range(len(text) + 1):
        print(text[:i])
        time.sleep(0.1)

    time.sleep(0.5)

    for i in range(len(text), -1, -1):
        print(text[:i])
        time.sleep(0.1)
