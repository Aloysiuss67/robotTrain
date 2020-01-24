import imageRec
import motorController
import picamera
import time
from gpiozero import Motor
import sys

motorLeft = Motor(17, 22)

camera = picamera.PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)


def main(args):
    debug_mode = False
    if args == "debug":
        debug_mode = True
    global camera
    global motorLeft
    time.sleep(1)  # time for camera to warm up
    count = 0
    while count < 100:
        error = imageRec.main(camera, debug_mode)
        # motorController.adjust_with_error(motorLeft, error) TODO enable for motor control
        count += 1
        time.sleep(0.1) # allow error rate make changes


if __name__ == "__main__":
   main(sys.argv[1])
