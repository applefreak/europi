#!/usr/bin/env python
from time import sleep
import signal

import Adafruit_SSD1306
import RPi.GPIO as GPIO
from menu import Menu

disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
menu = Menu(disp, { 'pin1': 14, 'pin2': 15, 'sw': 4 }, ['Bluetooth Setup...', 'Record...', 'Shutdown', 'trolol', 'zomg'])

def term_handler (arg1, ar2):
    GPIO.cleanup()
    print("Exiting...")
    exit()

signal.signal(signal.SIGTERM, term_handler)
signal.signal(signal.SIGINT, term_handler)

while 1:
    sleep(0.1)
