import cv2
import os
from tkinter import filedialog
import numpy as np

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*png"),("JPEG","*jpeg"),("JPG","*.jpg"),("BMP","*bmp")))

img = cv2.imread(fullPATH)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(gray,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

cv2.imshow("Original Image",img)
cv2.imshow("Gray Scaled",gray)
cv2.imshow("Laplacian",lap)

cv2.waitKey(0)
