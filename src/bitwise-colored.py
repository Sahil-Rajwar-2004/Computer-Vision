import cv2
import os
from tkinter import filedialog

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fulllPATH1 = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("BMP","*.bmp")))
fulllPATH2 = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("BMP","*.bmp")))

img1 = cv2.imread(fulllPATH1)
img2 = cv2.imread(fulllPATH2)

img1_resized = cv2.resize(img1,(img2.shape[1],img2.shape[0]))

cv2.imshow("Image1",img1_resized)
cv2.imshow("Image2",img2)

OR = cv2.bitwise_or(img1_resized,img2)
cv2.imshow("OR",OR)

AND = cv2.bitwise_and(img1_resized,img2)
cv2.imshow("AND",AND)

NOT = cv2.bitwise_not(img1_resized,img2)
cv2.imshow("NOT",NOT)

XOR = cv2.bitwise_xor(img1_resized,img2)
cv2.imshow("XOR",XOR)

cv2.waitKey(0)
cv2.destroyAllWindows()
