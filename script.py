import pyautogui
import json
import time
import keyboard 

# Load points
with open("points.json", "r") as f:
    points = json.load(f)

# Get image bounds - optimized to use single pass
min_x = min_y = float('inf')
max_x = max_y = float('-inf')
for x, y in points:
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

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
pyautogui.PAUSE = 0.001  # Reduced from 0.005 for faster execution

# Pre-calculate all coordinates for better performance
print(f"📊 Processing {len(points)} points...")
start_time = time.time()

coordinates = [
    (int((x - min_x) * scale + offset_x), int((y - min_y) * scale + offset_y))
    for x, y in points
]

prep_time = time.time() - start_time
print(f"⚡ Coordinates calculated in {prep_time:.2f} seconds")
print("🖌️  Starting to draw...")

draw_start = time.time()
# Use click with coordinates directly - faster than moveTo + click
for draw_x, draw_y in coordinates:
    pyautogui.click(draw_x, draw_y)

draw_time = time.time() - draw_start
total_time = time.time() - start_time

print(f"✅ Done!")
print(f"⏱️  Drawing time: {draw_time:.2f} seconds")
print(f"⏱️  Total time: {total_time:.2f} seconds")
print(f"📈 Average time per point: {(draw_time/len(points)*1000):.2f} ms")
