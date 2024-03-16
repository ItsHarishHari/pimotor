import gpiod
from time import sleep

# Define the chip and line numbers
chip = "gpiochip0"
ENA = 17
IN1 = 27
IN2 = 22

# Open the chip
chip_dev = gpiod.Chip(chip)

# Get the lines
ENA_line = chip_dev.get_line(ENA)
IN1_line = chip_dev.get_line(IN1)
IN2_line = chip_dev.get_line(IN2)

# Request output for the lines
ENA_line.request(consumer="motor_control", type=gpiod.LINE_REQ_DIR_OUT)
IN1_line.request(consumer="motor_control", type=gpiod.LINE_REQ_DIR_OUT)
IN2_line.request(consumer="motor_control", type=gpiod.LINE_REQ_DIR_OUT)

def forward():
    ENA_line.set_value(1)
    IN1_line.set_value(1)
    IN2_line.set_value(0)

def backward():
    ENA_line.set_value(1)
    IN1_line.set_value(0)
    IN2_line.set_value(1)

while True:
    forward()
    sleep(1)
    backward()
    sleep(1)
