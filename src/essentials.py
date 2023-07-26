from tkinter import filedialog
import cv2
import os

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg"),("BMP","*.bmp")))

img = cv2.imread(fullPATH)
cv2.imshow("Engine",img)

# from colored to gray scaled color
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscaled Engine",gray)

# blur
blur = cv2.GaussianBlur(img,(101,101),cv2.BORDER_DEFAULT) # ksize = (odd,odd)
cv2.imshow("blurred Engine",blur)

# Edges cascading
cascade = cv2.Canny(img,125,175)
cv2.imshow("edges Engine",cascade)

# dialating img
dialated = cv2.dilate(cascade,(3,3),iterations = 4)
cv2.imshow("dialated Engine",dialated)

cv2.waitKey()
cv2.destroyAllWindows()
