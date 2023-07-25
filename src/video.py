import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    exit()

running = True
while running:
    ret,frame = cap.read()
    if not ret:
        running = False
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # color to gray
    cv2.imshow("frame",gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        running = False

cap.release()
cv2.destroyAllWindows()
