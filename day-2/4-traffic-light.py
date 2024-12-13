from machine import Pin
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Red
red.value(1)
amber.value(0)
green.value(0)

time.sleep(5)

# Red Amber
red.value(1)
amber.value(1)
green.value(0)

time.sleep(2)

# Green
red.value(0)
amber.value(0)
green.value(1)

time.sleep(5)

# Amber
red.value(0)
amber.value(1)
green.value(0)

time.sleep(3)

# Red
red.value(1)
amber.value(0)
green.value(0)

time.sleep(5)

red.value(0)
amber.value(0)
green.value(0)