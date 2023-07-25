from tkinter import filedialog
import cv2
import os

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes=(("MP4","*.mp4"),("AVI","*.avi")))

cap = cv2.VideoCapture(fullPATH)

def rescaling(frame,scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    return cv2.resize(frame,(width,height),interpolation = cv2.INTER_AREA)

if not cap.isOpened():
    exit()

running = True
while running:
    ret,frame = cap.read()
    if not ret:
        running = False
    rescaled_vid = rescaling(frame)
    cv2.imshow("org frame",frame)
    cv2.imshow("scaled frame",rescaled_vid)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        running = False

cap.release()
cv2.destroyAllWindows()
