import time
from pynput import keyboard
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--target', help = "target to display counter" )
args = parser.parse_args()

target = args.target
# detect wether space key is pressed or not
is_space_pressed = False
def on_press(key):
    global is_space_pressed
    if key == keyboard.Key.space:
        print("You stopped counter using space key")
        is_space_pressed = True
        return False

listener = keyboard.Listener(on_press = on_press)
listener.start()

# increment every second until it equals the input
count = 0
while count < int(target) and (not is_space_pressed):
    count += 1
    print("Counter:", count)
    time.sleep(1)

listener.stop()