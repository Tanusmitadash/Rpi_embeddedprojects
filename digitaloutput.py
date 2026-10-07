from gpiozero import DigitalOutputDevice
from time import sleep

output = DigitalOutputDevice(27)

output.on()
print("OUTPUT ON")

sleep(2)

output.off()
print("OUTPUT OFF")
