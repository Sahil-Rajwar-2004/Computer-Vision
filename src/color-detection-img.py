import cv2
import os
import numpy as np
from tkinter import filedialog

"""
    RED:
        Lower: [0, 100, 100]
        Upper: [10, 255, 255]

        Lower: [160, 100, 100]
        Upper: [180, 255, 255]

    Green:
        Lower: [40, 40, 40]
        Upper: [80, 255, 255]

    Blue:
        Lower: [100, 50, 50]
        Upper: [130, 255, 255]

    Yellow:
        Lower: [20, 100, 100]
        Upper: [40, 255, 255]

    Orange:
        Lower: [10, 100, 100]
        Upper: [25, 255, 255]

    Purple:
        Lower: [130, 40, 40]
        Upper: [170, 255, 255]

    Pink:
        Lower: [150, 40, 40]
        Upper: [170, 255, 255]
"""


filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fulllPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("BMP","*.bmp")))

img = cv2.imread(fulllPATH)
hsvIMG = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lowerBlue = np.array([100,50,50])
higherBlue = np.array([130,255,255])

mask = cv2.inRange(hsvIMG,lowerBlue,higherBlue)
blues = cv2.bitwise_and(img,img,mask = mask)

cv2.imshow("Orginial Image",img)
cv2.imshow("Blues",blues)

cv2.waitKey(0)
cv2.destroyAllWindows()
