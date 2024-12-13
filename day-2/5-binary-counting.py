from machine import Pin
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

wait = 1

# 1
red.value(1)
amber.value(0)
green.value(0)

time.sleep(wait)

# 2
red.value(0)
amber.value(1)
green.value(0)

time.sleep(wait)

# 3
red.value(1)
amber.value(1)
green.value(0)

time.sleep(wait)

# 4
red.value(0)
amber.value(0)
green.value(1)

time.sleep(wait)

# 5
red.value(1)
amber.value(0)
green.value(1)

time.sleep(wait)

# 6
red.value(0)
amber.value(1)
green.value(1)

time.sleep(wait)

# 7
red.value(1)
amber.value(1)
green.value(1)

time.sleep(wait)

# Off
red.value(0)
amber.value(0)
green.value(0)
