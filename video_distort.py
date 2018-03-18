import cv2, time
import numpy as np

# @args
# 0, 1, 2 = attached camera id
# "filename.avi"
video = cv2.VideoCapture( 0 )

while True:
    check, frame = video.read()
    # print( check )
    # print( frame )

    rows, cols, ch = frame.shape
    # print( rows )

    # pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    # pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    pts1 = np.float32([[212,293],[587,245],[194,480],[623,480]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

    M   = cv2.getPerspectiveTransform( pts1, pts2 )
    dst = cv2.warpPerspective( frame, M, ( 300, 300 ) )


    # Display processed frame
    cv2.imshow( "Feed", frame )
    cv2.imshow( "Warped", dst )

    # Press q to quit
    key = cv2.waitKey( 1 )
    if key == ord( "q" ):
        break


# release resource after use
video.release()
# Close any open windows
cv2.destroyAllWindows