from gpiozero import DigitalInputDevice, LED
from time import sleep

entry_sensor = DigitalInputDevice(17)
chamber_sensor = DigitalInputDevice(22)
exit_sensor = DigitalInputDevice(23)

illumination = LED(27)


while True:

    # Step 1: Check entry
    if entry_sensor.is_active:

        print("Slide detected at entry")

        # Step 2: Check chamber
        if chamber_sensor.is_active:

            print("Chamber closed")

            # Step 3: Turn illumination ON
            illumination.on()

            print("Illumination ON")

        else:

            print("WARNING: Chamber open")

            illumination.off()

    else:

        illumination.off()

        print("Waiting for slide")

    sleep(0.1)
    
    #hardware abstraction
    class MockGPIO:

    def read_sensor(self):
        return True

    def turn_illumination_on(self):
        print("SIMULATION: Illumination ON")

    def turn_illumination_off(self):
        print("SIMULATION: Illumination OFF")
