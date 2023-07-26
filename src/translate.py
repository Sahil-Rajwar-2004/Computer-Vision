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

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1],img.shape[0])
    return cv2.warpAffine(img,transMat,dim)

translated = translate(img,100,100)
cv2.imshow("Translated",translated)

cv2.waitKey(0)
cv2.destroyAllWindows()
