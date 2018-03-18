import cv
import sys
import os
import time
camera_index = 0 
capture = cv.CaptureFromCAM(camera_index)
count = 0
def repeat():
    global capture
    global camera_index
    global count
    frame = cv.GetMat(cv.QueryFrame(capture))
    framegray = cv.CreateMat(480, 640, cv.CV_8UC1)
    cv.CvtColor(frame, framegray, cv.CV_BGR2GRAY)
    sys.stdout.write(framegray.tostring())
    c = cv.WaitKey(1)
    if c == 27:
        print count
        sys.exit()

while True:
    repeat()


# pipe to 
# python capturewebcam.py | ffmpeg -f rawvideo -pix_fmt gray -s 640x480 -i - -an -f rawvideo -r 10 "/dev/null"


# or
# ./app | ffmpeg -re -i pipe:0 -f v4l2 /dev/video1


# python domvid.py | ffmpeg -f rawvideo -s 640x480 -i - -an -f v4l2 /dev/video0