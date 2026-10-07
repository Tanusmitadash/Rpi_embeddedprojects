from gpiozero import DigitalInputDevice, DigitalOutputDevice
from time import sleep

entry = DigitalInputDevice(17)
chamber = DigitalInputDevice(22)
exit_sensor = DigitalInputDevice(23)

illumination = DigitalOutputDevice(27)
camera_trigger = DigitalOutputDevice(24)


while True:

    if entry.is_active:

        print("Slide detected")

        if chamber.is_active:

            print("Chamber closed")

            illumination.on()

            print("Illumination ON")

            camera_trigger.on()
            sleep(0.01)
            camera_trigger.off()

            print("Camera trigger sent")

        else:

            print("Chamber open")
            illumination.off()

    else:

        illumination.off()

    sleep(0.1)
