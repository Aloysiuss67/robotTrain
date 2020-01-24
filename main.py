import imageRec
import motorController
import picamera
import time
from gpiozero import Motor

motorLeft = Motor(17, 22)

camera = picamera.PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)


def main():
    global camera
    global motorLeft
    time.sleep(1)  # time for camera to warm up
    count = 0
    while count < 100:
        error = imageRec.main(camera)
        motorController.adjust_with_error(motorLeft, error)
        count += 1
        time.sleep(0.1) # allow error rate make changes


main()
