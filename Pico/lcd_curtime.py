# Copyright 2022 Gabrian Chua
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
import busio
import time

i2c = busio.I2C(board.GP1, board.GP0)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

while True:
    lcd.clear()
    curtime = time.localtime()
    hr = curtime.tm_hour % 12
    ampm = "PM"
    if hr == curtime.tm_hour:
        ampm = "AM"
    lcd.print(str(hr) + ":" + str(curtime.tm_min) + ":" + str(curtime.tm_sec) + " " + ampm)
    time.sleep(1)