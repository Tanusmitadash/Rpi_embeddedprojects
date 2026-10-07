from gpiozero import DigitalInputDevice, DigitalOutputDevice
from time import sleep

sensor = DigitalInputDevice(17)
illumination = DigitalOutputDevice(27)

while True:

    if sensor.is_active:

        illumination.on()
        print("Sensor detected → Illumination ON")

    else:

        illumination.off()
        print("No sensor → Illumination OFF")

    sleep(0.1)
