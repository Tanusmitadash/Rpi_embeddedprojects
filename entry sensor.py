from gpiozero import DigitalInputDevice
from time import sleep

sensor = DigitalInputDevice(17)

while True:

    if sensor.is_active:
        print("Sensor ON")
    else:
        print("Sensor OFF")

    sleep(0.1)
