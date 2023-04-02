import cv2
import time

vid = cv2.VideoCapture(0)
old_time=time.time()

while(True):

    ret, frame = vid.read()
    new_time=time.time()


    cv2.imshow('frame', frame)
    if(new_time-old_time>2):
        cv2.imwrite("curr_img.png",frame)
        old_time=time.time()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()