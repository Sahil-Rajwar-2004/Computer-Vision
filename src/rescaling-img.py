from tkinter import filedialog
import cv2
import os

filePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*png"),("JPEG","*jpeg"),("JPG","*.jpg"),("BMP","*bmp")))

img = cv2.imread(fullPATH)

def rescaling(frame,scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    return cv2.resize(frame,(width,height),interpolation = cv2.INTER_AREA)

rescaled_img = rescaling(img,scale = 0.75)

cv2.imshow("original image",img)
cv2.imshow("rescaled image",rescaled_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
