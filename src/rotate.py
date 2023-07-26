import numpy as np
import cv2
import os
from tkinter import filedialog

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fulllPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("BMP","*.bmp")))

img = cv2.imread(fulllPATH)
cv2.imshow("Engine",img)

def rotate(img,angle):
    height,width = img.shape[:2]
    rotMat = cv2.getRotationMatrix2D((width/2,height/2),angle,1)
    return cv2.warpAffine(img,rotMat,(width,height))

rotated = rotate(img,180)
cv2.imshow("Rotated",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
