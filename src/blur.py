import cv2
import os
from tkinter import filedialog

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fulllPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("BMP","*.bmp")))

# Original Image
img = cv2.imread(fulllPATH)
cv2.imshow("Org Img",img)

# Average Blur
avg = cv2.blur(img,(7,7))
cv2.imshow("Avg Blur",avg)

# Gaussian Blur
gauss = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gaussian Blur",gauss)

# Median Blur
median = cv2.medianBlur(img,7)
cv2.imshow("Median Blur",median)


cv2.waitKey(0)
