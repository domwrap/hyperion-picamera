import cv2, time

# Face detection template
cascade_face = cv2.CascadeClassifier( "haarcascade_frontalface_default.xml" )

# @args
# 0, 1, 2 = attached camera id
# "filename.avi"
video = cv2.VideoCapture( 0 )

while True:
    check, frame = video.read()

    print( check )
    print( frame )

    # Insert pause
    # time.sleep( 3 )

    # Convert frame to greyscale
    bw = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )

    # Display processed frame
    cv2.imshow( "Capturing", bw )

    # Press ! to quit
    key = cv2.waitKey( 1 )
    if key == ord( "q" ):
        break

# release resource after use
video.release()
# Close any open windows
cv2.destroyAllWindows