import picamera
import picamera.array
import time
import cv2
import numpy as np

colourThreshold = 40  # white is high (255)
scale = 0.0009
error = 0.0

camera = picamera.PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)


def main():
    time.sleep(1)  # time for camera to warm up
    count = 0

    while count < 100:
        img = snapshot()
        line_detection(img)
        count += 1


def snapshot():
    raw_capture = picamera.array.PiRGBArray(camera)
    camera.capture(raw_capture, format="bgr", use_video_port=True)
    img = raw_capture.array
    return img


def line_detection(img):
    global error
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    white_count = 0

    for i in range(0, 640, 40):
        if gray[370, i] > colourThreshold:  # if greater, the pixel is white (white = 255, black = 0)
            print('1', end='')
            pixel_col = 1
            white_count += 1  # count
        else:
            print('0', end='')
            pixel_col = 0

        error = error + (i - 300) * pixel_col
    print('')
    error = error * scale
    print(error)
