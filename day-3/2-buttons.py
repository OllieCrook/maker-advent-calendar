from machine import Pin
import time

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True:
    time.sleep(0.2)

    if button1.value() == 1:
        print("Button 1 Pressed")

    if button2.value() == 1:
        print("Button 2 Pressed")

    if button3.value() == 1:
        print("Button 3 Pressed")
