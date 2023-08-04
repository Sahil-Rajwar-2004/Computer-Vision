from tkinter import filedialog
import os
import numpy as np
import cv2

filePATH = "assetes\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,filePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*png"),("JPEG","*jpeg"),("JPG","*.jpg"),("BMP","*bmp")))

img = cv2.imread(fullPATH)
grayScaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grayScaled,100,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("Original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
