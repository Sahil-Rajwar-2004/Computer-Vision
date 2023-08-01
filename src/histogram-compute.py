import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from tkinter import filedialog

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("BMP","*.bmp")))

img = cv2.imread(fullPATH)
cv2.imshow("Original Image",img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale Image",gray)

grayHist = cv2.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("bins")
plt.ylabel("number of pixels")
plt.plot(grayHist)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
