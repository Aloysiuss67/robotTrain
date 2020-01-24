import picamera
import picamera.array
import time
import cv2
import numpy as np

colourThreshold = 40  # white is high (255)
scale = 0.0009
error = 0.0

debugMode = True;


def main(camera):
    img = snapshot(camera)
    return line_detection(img)


def snapshot(camera):
    raw_capture = picamera.array.PiRGBArray(camera)
    camera.capture(raw_capture, format="bgr", use_video_port=True)
    img = raw_capture.array
    return img


def line_detection(img):
    global error
    global colourThreshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for i in range(0, 640, 40):
        if gray[370, i] > colourThreshold:  # if greater, the pixel is white (white = 255, black = 0)
            if debugMode:
                print('1', end='')
            pixel_col = 1
        else:
            if debugMode:
                print('0', end='')
            pixel_col = 0

        error = error + (i - 300) * pixel_col
    error = error * scale

    if debugMode:
        print('')
        print(error)

    return error
