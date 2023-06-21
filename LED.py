# Load the 'machine' module to access the hardware
import machine

# Load the 'time' module which includes the 'sleep' class
import time

# Create an 'led' object in pin 2
# and set the pin direction to output
led = machine.Pin(2, machine.Pin.OUT)

# Create an eternal loop that blinks the LED
# time.sleep(0.5) creates a 0.5 second delay
# or 500 milli seconds
while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)