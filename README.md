# hyperion-picamera
Interstitial program to capture and transform a video feed to use as Hyperion LED source

### Test commands

```
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt yuyv422 -i - -an -f v4l2 /dev/video0
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt yuv420p -i - -an -f v4l2 /dev/video0
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt uyvy422 -i - -an -f v4l2 /dev/video0
```


### WORKING

```
# python domvid.py | ffmpeg -f rawvideo -s 640x480 -pix_fmt bgr24 -i - -an -f v4l2 -pix_fmt uyvy422 /dev/video0
# streamer -f jpeg -s 640x480 -o out_uyvy.jpeg
# v4l2-ctl --all
```