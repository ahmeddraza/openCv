import cv2
import numpy as np

img = cv2.imread("pic.jpg")
temp_img = img.copy()
flag = False
ix = -1
iy = -1


def draw(event,x,y,flags,params):
    global flag, ix, iy,img,temp_img
    if(event==1):
        flag = True
        ix = x
        iy= y
        temp_img = img
        
    elif (event==0):
        if (flag == True):
            img = temp_img.copy()
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),thickness=1,color=(0,0,0))
    elif (event ==4):
        fx,fy = x,y
        flag = False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),thickness=1,color=(0,0,0))
        new_img = img[iy:fy,ix:fx]
        cv2.imshow("New_Image",new_img)
        cv2.waitKey(0)
        


cv2.imshow("Window",img)
cv2.namedWindow(winname="Window")
cv2.setMouseCallback("Window",draw)
while True:
    cv2.imshow("Window",img)
    if(cv2.waitKey(1) & 0xFF==ord('x')):
        break
cv2.destroyAllWindows()