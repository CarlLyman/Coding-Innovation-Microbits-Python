# 02.2 Gestures Events
# by C Lyman
# July 2019

# Much better versions for Gesture Events
#   Uses was_gesture and then an if statement.
#   It uses only the last item in the buffer.

from microbit import *

while True:
    # Event gesture face up
    faceUp = accelerometer.was_gesture("face up")
    if faceUp:
        display.scroll("UP")
    
    # Event gesture face down
    faceDown = accelerometer.was_gesture("face down")
    if faceDown:
        display.scroll("DWN")
        
    # Event gesture shake
    shake = accelerometer.was_gesture("shake")
    if shake:
        display.scroll("SHK")
        
    # Event gesture up
    up = accelerometer.was_gesture("up")
    if up:
        display.scroll("^")
        
    # Event gesture down
    down = accelerometer.was_gesture("down")
    if down:
        display.show("v")
        
    # Event gesture right
    right = accelerometer.was_gesture("right")
    if right:
        display.show(">")
        
    # Event gesture left
    left = accelerometer.was_gesture("left")
    if left:
        display.show("<")
        
    
