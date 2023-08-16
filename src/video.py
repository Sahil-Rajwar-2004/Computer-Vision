import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640) # set width
cap.set(4,480) # set height
cap.set(10,100) # set brightness

if not cap.isOpened():
    exit()

running = True
while running:
    ret,frame = cap.read()
    if not ret:
        running = False
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        running = False

cap.release()
cv2.destroyAllWindows()
