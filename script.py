import pyautogui
import json
import time
import pynput

# Retrieve json
with open("points.json", "r") as f:
    points = json.load(f)


# Get boarder

input()
x1, y1 = pyautogui.position()

print(x1, y1)

input()
x2, y2 = pyautogui.position()
print(x2,y2)