# import the necessary packages
from picamera.array import PiRGBArray
# from picamera.array import PiYUVArray
from picamera import PiCamera
import time
import cv2
import sys
import os


count = 0


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(640, 480))
# rawCapture = PiYUVArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)



# capture frames from the camera
for frame in camera.capture_continuous( rawCapture, format="bgr", use_video_port=True ):
# for frame in camera.capture_continuous( rawCapture, format="yuv", use_video_port=True ):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	# convert color space for Hyperion compatability
	# imageYUV = cv2.cvtColor( image, cv2.COLOR_BGR2YUV )

	# write the frame
	sys.stdout.write( image.tostring() )

	# Grab keypress so know when to quit
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	if key == 27:
		print( count )
		sys.exit()





# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt yuyv422 -i - -an -f v4l2 /dev/video0
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt yuv420p -i - -an -f v4l2 /dev/video0
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt uyvy422 -i - -an -f v4l2 /dev/video0





# WORKING
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt bgr24 -i - -an -f v4l2 -pix_fmt uyvy422 /dev/video0
# streamer -f jpeg -s 640x480 -o out_uyvy.jpeg
# v4l2-ctl --all

