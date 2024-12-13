from machine import Pin
import time

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True:
    time.sleep(0.2)

    if button1.value() == 1 and button2.value() == 1:
        green.value(1)
        red.value(0)
    elif button1.value() == 1:
        amber.value(1)
        red.value(0)
    else:
        red.value(1)
        amber.value(0)
        green.value(0)
