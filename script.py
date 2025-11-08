import pyautogui
import json
import time
import keyboard 

# Load points
with open("points.json", "r") as f:
    points = json.load(f)

# Get image bounds
xs = [p[0] for p in points]
ys = [p[1] for p in points]
min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)
img_width = max_x - min_x
img_height = max_y - min_y

# Ask user for border points using mouse position 
print("Move your mouse to the TOP-LEFT corner, then press ENTER...")
keyboard.wait("enter")
x1, y1 = pyautogui.position()
print(f"Top-left set at ({x1}, {y1})")

print("Now move your mouse to the BOTTOM-RIGHT corner, then press ENTER...")
keyboard.wait("enter")
x2, y2 = pyautogui.position()
print(f"Bottom-right set at ({x2}, {y2})")

# Compute drawing box and scale
draw_width = abs(x2 - x1)
draw_height = abs(y2 - y1)
offset_x = min(x1, x2)
offset_y = min(y1, y2)

scale_x = draw_width / img_width
scale_y = draw_height / img_height
scale = min(scale_x, scale_y)

# Fail-safe & pause 
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.005

for (x,y) in points:
    draw_x = int((x - min_x) * scale + offset_x)
    draw_y = int((y - min_y) * scale + offset_y)

    pyautogui.moveTo(draw_x, draw_y)
    pyautogui.click()

print("✅ Done!")
