from tkinter import filedialog
import cv2
import os

imagePATH = "assets\\"
mainPATH = os.getcwd()
absPATH = os.path.join(mainPATH,imagePATH)

fullPATH = filedialog.askopenfilename(initialdir = absPATH,filetypes = (("PNG","*png"),("JPEG","*jpeg"),("JPG","*.jpg"),("BMP","*bmp")))

img = cv2.imread(fullPATH,0) # Black and White kind of
"""
    cv2.IMREAD_COLOR = 1            # Loads a color image
    cv2.IMREAD_GRAYSCALE = 0        # Loads image in grayscale mode
    cv2.IMREAD_UNCHANGED = -1       # Loads image as such including alpha channel
"""
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
