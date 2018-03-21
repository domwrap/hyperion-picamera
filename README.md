# hyperion-picamera
Interstitial program to capture and transform a video feed to use as Hyperion LED source

# WARNING

`NOTE: This is a pre-alpha, work-in-progress, hobby project and does not (yet) work locally, nor is it destined (yet) to work for anybody else.`


## Introduction

I have had a [Hyperion](https://github.com/hyperion-project) ambilight installation for several years but when I recently moved to a new 4K HDR tv none of my streaming or local media would play very well on existing sources, and my AVR is not very 4K compatible (only 30fps, no HDR). Furthermore, my TV only has one "good" HDMI port that supports HDR in but also ARC out which further complicates things.

As a result I've ended up playing almost all of my content through the TV's built in apps which are actually very good, but cannot be captured to work with Hyperion.

This is my attempt to circumvent that problem and make an all-source solution to Hyperion by using a RasPi + camera pointing at the TV to capture what is actually on screen and feeding that to Hyperion.


## Requirements

- RasPi + Camera pointed at screen
- Image skew, as camera will never be 100% straight on to TV
- Compatible output stream for Hyperion
- Minimal lag otherwise it's all pointless as the LEDs will be behind the picture
- To help with lag, stream can be very low resolution (match # of LEDs), and can also be fairly low framerate (10fps)

## To Do

- ~~Capture TV display using RasPi + cam~~
- ~~Distort off-axis captured image in to a usable rectangle~~
- ~~Make YUYV Hyperion compatible stream~~
- ~~Create virtual `/dev/videoX` interface for Hyperion~~
- Successfully read virtual device with Hyperion ***CURRENTLY STUCK HERE***
- Possibly needed: increase contrast and deepen blacks so Hyperion black-bar detection works automagically
- Allow auto-configure of TV corners using computer vision reference points (QR stickers?). This will allow easy recalibration of the tool if the TV or camera is moved


## Work In Progress

### Test Output Commands

```
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt yuyv422 -i - -an -f v4l2 /dev/video0
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt yuv420p -i - -an -f v4l2 /dev/video0
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt uyvy422 -i - -an -f v4l2 /dev/video0
```


### Latest Working Progress

```
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt bgr24 -i - -an -f v4l2 -pix_fmt uyvy422 /dev/video0
# streamer -f jpeg -s 640x480 -o out_uyvy.jpeg
# v4l2-ctl --all
```
