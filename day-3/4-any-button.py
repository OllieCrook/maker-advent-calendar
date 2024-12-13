from machine import Pin
import time

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

green = Pin(20, Pin.OUT)

while True:
    time.sleep(0.2)

    if button1.value() == 1 or button2.value() == 1 or button3.value() == 1:
        green.value(1)
        time.sleep(2)
        green.value(0)
