import cv2
import os

filePATH = "assets\\ironman.mp4"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

cap = cv2.VideoCapture(absPATH)

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
