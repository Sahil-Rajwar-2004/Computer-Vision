import cv2

cap = cv2.VideoCapture(0)

running = True
while running:
    ret,frame = cap.read()
    if not ret:
        running = False
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # color to HSV(Hue Saturation Value)
    cv2.imshow("frame",gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        running = False

cap.release()
cv2.destroyAllWindows()
