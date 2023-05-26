# Copyright 2023 Gabrian Chua
import time
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio
from os import urandom
import math
import time

# consts
mouse_speed = 2 # takes 2 seconds each movement
mouse_res = 100 # each movement is split into 100 minimovements
mouse_wait = 1/60 # 60 updates per second
keyboard_delay = 1 # how long to wait between keystrokes
keyboard_press_time = 0.1 # how long each key is pressed
alt_tab_frequency = 30 # alt tab every 30 jiggles

# vars
jiggle_iteration = 0

# setup mouse and led
mouse = Mouse(usb_hid.devices)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# blink led to allow to cancel code
print("5 second cooldown to stop code...")
for i in range(5):
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

# setup keyboard
# must be after wait to avoid race condition
keyboard = Keyboard(usb_hid.devices)

try:
    led.value = True
    while True:
        rand = urandom(2)
        print("moving to target", rand[0] - 128, rand[1] - 128)
        moveX = math.ceil((rand[0] - 128) / mouse_res)
        moveY = math.ceil((rand[1] - 128) / mouse_res)
        if (moveX <= 0):
            moveX = -1
        if (moveY <= 0):
            moveY = -1
        for i in range(mouse_res):
            mouse.move(moveX, moveY)
            time.sleep(mouse_wait)
        jiggle_iteration += 1
        if jiggle_iteration == alt_tab_frequency:
            keyboard.press(Keycode.ALT, Keycode.TAB)
            time.sleep(keyboard_press_time)
            keyboard.release_all()
            jiggle_iteration = 0
finally:
    led.value = False


