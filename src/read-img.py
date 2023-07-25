import cv2
import os

mainPATH = os.getcwd()
imagePATH = "assets\\messi5.jpg"
absPATH = os.path.join(mainPATH,imagePATH)


img = cv2.imread(absPATH,0) # Black and White kind of
"""
    cv2.IMREAD_COLOR = 1            # Loads a color image
    cv2.IMREAD_GRAYSCALE = 0        # Loads image in grayscale mode
    cv2.IMREAD_UNCHANGED = -1       # Loads image as such including alpha channel
"""
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
