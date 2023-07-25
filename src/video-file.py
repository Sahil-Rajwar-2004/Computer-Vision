from tkinter import filedialog
import cv2
import os

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("MP4","*.mp4"),("AVI","*.avi")))

cap = cv2.VideoCapture(fullPATH)

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
