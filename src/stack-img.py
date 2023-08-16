import cv2
import numpy as np
from tkinter import filedialog
import os

imgPATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,imgPATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = [("PNG","*.png"),("JPEG","*.jpeg"),("JPG","*.jpg"),("BMP","*.bmp")])

img = cv2.imread(fullPATH)
cv2.imshow("orginal image",img)

stkImgHor = np.hstack((img,img))
cv2.imshow("horizontally stacked img",stkImgHor)

stkImgVer = np.vstack((img,img))
cv2.imshow("vertically stacked img",stkImgVer)

cv2.waitKey(0)
cv2.destroyAllWindows()


