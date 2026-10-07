from gpiozero import Button

sensor = Button(17, pull_up=True)

while True:

    if sensor.is_pressed:
        print("Sensor activated")
