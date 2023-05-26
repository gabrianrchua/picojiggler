# Copyright 2022 Gabrian Chua
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import time

# little delay before init
print('waiting 1 second before init')
time.sleep(1)
mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

def mouse_move(x, y):
    mouse.move(x, -y)

def mouse_scroll(amt):
    mouse.move(wheel=amt)

def mouse_click(btn):
    if btn == 'l':
        mouse.click(Mouse.LEFT_BUTTON)
    elif btn == 'r':
        mouse.click(Mouse.RIGHT_BUTTON)
    elif btn == 'm':
        mouse.click(Mouse.MIDDLE_BUTTON)
    else:
        print('invalid mouse button:', btn)

def print_help():
    print('/h -- this help menu')
    print('/m 123 123 -- move mouse x, y')
    print('/k text here 123 -- type text')
    print('/c l|r|m -- click left right middle')
    print('/s 123 -- scroll. positive=up, negative=down')
    print('/x -- exit')
    print('exit -- exit')

try:
    while True:
        cmd = input('mnk> ')
        cmds = cmd.strip().split(' ')
        if cmds[0] == '/m':
            mouse_move(int(cmds[1]), int(cmds[2]))
        elif cmds[0] == '/h':
            print_help()
        elif cmds[0] == '/c':
            mouse_click(cmds[1])
        elif cmds[0] == '/k':
            keyboard_layout.write(cmd[3:])
        elif cmds[0] == '/s':
            mouse_scroll(int(cmds[1]))
        elif cmds[0] == '/x' or cmds[0] == 'exit':
            break
        else:
            print_help()
finally:
    keyboard.release_all()