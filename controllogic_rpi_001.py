import time

slide_detected = False
chamber_closed = False
camera_ready = False


def start_illumination():
    print("Illumination ON")


def stop_illumination():
    print("Illumination OFF")


def start_camera():
    print("Camera ON")


def stop_camera():
    print("Camera OFF")


def move_stage():
    print("Stage moving...")
    time.sleep(2)
    print("Stage position reached")


def autofocus():
    print("Autofocus running...")
    time.sleep(2)
    print("Focus achieved")


def scan():
    print("Scanning...")
    time.sleep(5)
    print("Scan complete")


# Main control logic

print("WSI SYSTEM START")

slide_detected = True
chamber_closed = True
camera_ready = True


if slide_detected:

    print("Slide detected")

    if chamber_closed:

        print("Chamber closed")

        if camera_ready:

            print("System ready")

            start_illumination()

            move_stage()

            autofocus()

            start_camera()

            scan()

            stop_camera()

            stop_illumination()

            print("WSI PROCESS COMPLETE")

        else:

            print("ERROR: Camera not ready")

    else:

        print("ERROR: Chamber open")

else:

    print("Waiting for slide")
