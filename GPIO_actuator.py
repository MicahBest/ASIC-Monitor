import RPi.GPIO as GPIO
import time

# Set up the GPIO pin numbers
forward_pin = 23
backward_pin = 24

# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pins as output
GPIO.setup(forward_pin, GPIO.OUT)
GPIO.setup(backward_pin, GPIO.OUT)

# Define the commands to move the actuator forward and backward
forward_command = GPIO.HIGH
backward_command = GPIO.LOW

# Move the actuator forward
GPIO.output(forward_pin, forward_command)
time.sleep(1)

# Stop the actuator
GPIO.output(forward_pin, GPIO.LOW)
time.sleep(1)

# Move the actuator backward
GPIO.output(backward_pin, backward_command)
time.sleep(1)

# Stop the actuator
GPIO.output(backward_pin, GPIO.LOW)

# Clean up the GPIO pins
GPIO.cleanup()
