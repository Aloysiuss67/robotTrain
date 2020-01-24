import sys
import imageRec
import motorController
import picamera
import time
#from gpiozero import Motor


#motorLeft = Motor(17, 22)

camera = picamera.PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)


def main(debug_mode):
    global camera
    global motorLeft
    time.sleep(1)  # time for camera to warm up
    count = 0
    while count < 100:
        error = imageRec.detect_error(camera, debug_mode)
        # motorController.adjust_left(motorLeft, error, debug_mode) TODO enable for motor control
        # motorController.adjust_right(motorRight, error, debug_mode) TODO enable for motor control
        count += 1
        time.sleep(0.1) # allow error rate make changes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "debug":
            main(True)
        else:
            main(False)
    else:
        main(False)
