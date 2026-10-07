from gpiozero import Button
from time import sleep

entry = Button(17)
chamber = Button(22)
exit_sensor = Button(23)

while True:

    print(
        "Entry:", entry.is_pressed,
        "Chamber:", chamber.is_pressed,
        "Exit:", exit_sensor.is_pressed
    )

    sleep(0.5)
    
    #Raspberry Pi does not have a built-in general-purpose analog input, so you normally need an ADC.Temperature sensorPhotodiodePotentiometerAnalog position sensor
