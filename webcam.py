import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 20
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,fps,(640,480))

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow("webcam",frame)
    if(cv2.waitKey(1) & 0xFF == ord('x')):
        break

cv2.destroyAllWindows()