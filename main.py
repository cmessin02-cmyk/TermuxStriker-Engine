import ctypes
import time
import sys
import tty
import termios
import os
import random

# 1. Setup C++ Library
path = os.path.abspath("./libgame.so")
lib = ctypes.CDLL(path)
lib.init_world()

# 2. Keypress Detection Function
def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# 3. Game Setup
px, py = 10, 10
# Randomize Goal position for a "Biggy" challenge
gx, gy = random.randint(2, 17), random.randint(2, 17)
player_icon = ord('G')

print("🎮 GAME LOADING...")
time.sleep(1)

try:
    while True:
        # Pass both Player and Goal coordinates to C++
        lib.update_player(px, py, player_icon, gx, gy)
        lib.render()
        
        # WIN CHECK
        if px == gx and py == gy:
            print("\n" + "⭐"*15)
            print("🏆 GOAL!!!")
            print("You reached the target like MESSI!")
            print("⭐"*15)
            break

        # INPUT HANDLING
        key = get_char().lower()
        if key == 'w': py -= 1
        elif key == 's': py += 1
        elif key == 'a': px -= 1
        elif key == 'd': px += 1
        elif key == 'q': break
        
        # Collision Handling (Keep inside walls)
        px = max(1, min(18, px))
        py = max(1, min(18, py))

except KeyboardInterrupt:
    pass

print("\n🚀 System Cleaned Up.")
