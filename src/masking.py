import cv2
import os
import numpy as np
from tkinter import filedialog

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("BMP","*.bmp")))

img = cv2.imread(fullPATH)
cv2.imshow("Org Image",img)

blank = np.zeros(img.shape[:2],dtype = "uint8")

mask = cv2.circle(blank,(img.shape[1]//2,img.shape[0]//2),200,(255,255,255),-1)
cv2.imshow("Circle",mask)

masked = cv2.bitwise_and(img,img,mask = mask)
cv2.imshow("Masked Image",masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
