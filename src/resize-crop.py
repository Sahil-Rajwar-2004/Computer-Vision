from tkinter import filedialog
import numpy as np
import cv2
import os

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("BMP","*.bmp")))

img = cv2.imread(fullPATH)
cv2.imshow("original image",img)

resizedImg = cv2.resize(img,(1000,500))
cv2.imshow("resized image",resizedImg)

cropImg = img[0:200,200:500]
cv2.imshow("cropped image",cropImg)

cv2.waitKey()
cv2.destroyAllWindows()
