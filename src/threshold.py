import cv2
import os
from tkinter import filedialog

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*png"),("JPEG","*jpeg"),("JPG","*.jpg"),("BMP","*bmp")))

img = cv2.imread(fullPATH)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

threshold,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
threshold,threshINV = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
adpThreshold  = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)

cv2.imshow("Original",img)
cv2.imshow("Gray Scaled Img",gray)
cv2.imshow("Thresh",thresh)
cv2.imshow("Inverse Threshold",threshINV)
cv2.imshow("Adaptive Threshold",adpThreshold)

cv2.waitKey(0)
