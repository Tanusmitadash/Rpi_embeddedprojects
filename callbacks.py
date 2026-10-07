#event driven programming
#When the sensor changes, execute this function

from gpiozero import Button
from time import sleep

sensor = Button(17)


def sensor_detected():
    print("Slide detected!")


sensor.when_pressed = sensor_detected

while True:
    sleep(1)
