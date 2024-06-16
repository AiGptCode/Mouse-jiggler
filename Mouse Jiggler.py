import argparse
import sys
import time
import random
import pyautogui
import tkinter as tk
import tkinter.messagebox
import threading
import multiprocessing

# Ensure only one instance is running
instance_lock = multiprocessing.Lock()
if not instance_lock.acquire(blocking=False):
    print("Mouse Jiggler is already running. Aborting.")
    sys.exit(1)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Mouse Jiggler")
parser.add_argument("-j", "--jiggle", action="store_true", help="start with jiggling enabled")
parser.add_argument("-m", "--minimized", action="store_true", help="start minimized")
parser.add_argument("-z", "--zen", action="store_true", help="start with zen (invisible) jiggling enabled")
parser.add_argument("-s", "--seconds", type=int, default=60, help="set number of seconds for the jiggle interval")
args = parser.parse_args()

# Create GUI
root = tk.Tk()
root.title("Mouse Jiggler")
root.resizable(False, False)

# Variables for GUI
jiggling = tk.BooleanVar()
jiggling.set(args.jiggle)
zen_jiggle = tk.BooleanVar()
zen_jiggle.set(args.zen)
jiggle_period = tk.IntVar()
jiggle_period.set(args.seconds)

# Jiggle function
def jiggle():
    while True:
        if not jiggling.get():
            time.sleep(0.1)
            continue
        x_offset = random.randint(-10, 10)
        y_offset = random.randint(-10, 10)
        x, y = pyautogui.position()
        if zen_jiggle.get():
            pyautogui.moveRel(x_offset, y_offset, duration=0.5)  # invisible jiggle
        else:
            pyautogui.moveTo(x + x_offset, y + y_offset, duration=0.5)  # visible jiggle
        time.sleep(jiggle_period.get())

# Start/Stop button command
def toggle_jiggle():
    jiggling.set(not jiggling.get())

# GUI widgets
tk.Checkbutton(root, text="Jiggle", variable=jiggling, command=toggle_jiggle).pack()
tk.Checkbutton(root, text="Zen Jiggle", variable=zen_jiggle).pack()
tk.Label(root, text="Jiggle period (seconds)").pack()
tk.Spinbox(root, from_=1, to=60, textvariable=jiggle_period).pack()
start_button = tk.Button(root, text="Start", command=toggle_jiggle)
start_button.pack()

# Start jiggle thread
jiggle_thread = threading.Thread(target=jiggle)
jiggle_thread.start()

# Run GUI main loop
root.mainloop()

# Release instance lock before exiting
instance_lock.release()
