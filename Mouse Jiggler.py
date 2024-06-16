import pyautogui
import time
import random

def jiggle_mouse():
    while True:
        # Generate random offsets within a small range
        x_offset = random.randint(-10, 10)
        y_offset = random.randint(-10, 10)

        # Get the current mouse position
        x, y = pyautogui.position()

        # Move the mouse to the new position slowly
        pyautogui.moveTo(x + x_offset, y + y_offset, duration=random.uniform(0.5, 1.0))

        # Click the mouse to prevent the screen from locking
        pyautogui.click()

        # Wait a random amount of time before the next jiggle
        time.sleep(random.uniform(30, 60))

# Start the mouse jiggler
jiggle_mouse()
