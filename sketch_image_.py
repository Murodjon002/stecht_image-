#use web camera from mobile 
import cv2
import numpy as np
k_size=7
url = "https://172.20.23.147:8080/video"
cap = cv2.VideoCapture(url)
while(True):
    camera, frame = cap.read()
    if frame is not None:
    
        grey_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        invert_img=cv2.bitwise_not(grey_img)

        blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

        invblur_img=cv2.bitwise_not(blur_img)

        sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
        cv2.imshow("Frame", sketch_img)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()