import numpy as np
import cv2

cap = cv2.VideoCapture(0)
frame = []

obj_x = -2000
obj_y = -2000

crsr_x = -2000
crsr_y = -2000

crsrsize = 20
objsize = 20

def mark_object(event, x, y, flags, param):
    global obj_x, obj_y, crsr_x, crsr_y, objsize, crsrsize
    if event == cv2.EVENT_LBUTTONDOWN:
        obj_x = x
        obj_y = y
        objsize = crsrsize
    if event == cv2.EVENT_MOUSEMOVE:
        crsr_x = x
        crsr_y = y


cv2.namedWindow("frame")
cv2.setMouseCallback('frame', mark_object)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    cv2.rectangle(frame, (obj_x - objsize, obj_y - objsize), (obj_x + objsize, obj_y + objsize), (0, 0, 255), 2)
    cv2.rectangle(frame, (crsr_x - crsrsize, crsr_y - crsrsize), (crsr_x + crsrsize, crsr_y + crsrsize), (255, 255, 0), 1)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    if (key == ord('-')) and (crsrsize > 20):
        crsrsize -= 10
        key = 0
    if (key == ord('=')) and (crsrsize < 100):
        crsrsize += 10
        key = 0

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
