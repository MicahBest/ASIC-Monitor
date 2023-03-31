import serial
import time

# Initialize the serial connection to the Arduino
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to the name of your serial port

# Define the commands to move the actuator forward and backward
forward_command = b'f'
backward_command = b'b'

# Move the actuator forward
ser.write(forward_command)
time.sleep(1)

# Stop the actuator
ser.write(b's')
time.sleep(1)

# Move the actuator backward
ser.write(backward_command)
time.sleep(1)

# Stop the actuator
ser.write(b's')

# Close the serial connection
ser.close()
