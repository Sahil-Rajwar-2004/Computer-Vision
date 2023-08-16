import cv2
import numpy as np
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox as msg

canvas = np.ones((650,700,3),np.uint8)*255
drawing = False
color = (0,0,0)
running = True
radius = 10

def draw(event,x,y,flags,param):
    global drawing,color
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(canvas,(x, y),radius,color,-1)

def save():
    location = filedialog.asksaveasfilename(defaultextension = ".png",filetypes = [("PNG","*.png")])
    if location:
        cv2.imwrite(location,canvas)
        print(f"File saved at {location}!")

def penSize(change):
    global radius
    radius += change
    if radius <= 1:
        radius = 1

def customColor():
    global color
    rgbColor,_ = colorchooser.askcolor(title="Select Color")
    if rgbColor:
        bgrColor = (int(rgbColor[2]),int(rgbColor[1]),int(rgbColor[0]))
        color = bgrColor

cv2.namedWindow("Virtual Paint")
cv2.setMouseCallback("Virtual Paint",draw)

while running:
    cv2.imshow("Virtual Paint",canvas)
    key = cv2.waitKey(1)

    if key == 27:
        ask = msg.askyesno("Warn", "Want to save the file before quitting?")
        if ask:
            save()
        running = False
    elif key == ord("i"):
        msg.showinfo("Info","[i]: display this info\n[r]: red\n[g]: green\n[b]: blue\n[e]: erase\n[c]: clear\n[s]: save the file\n[+]: increase pen size\n[-]: decrease pen size\n[p]: customize the color")
    elif key == ord("r"):
        color = (0,0,255)
    elif key == ord("g"):
        color = (0,255,0)
    elif key == ord("b"):
        color = (255,0,0)
    elif key == ord("e"):
        color = (255,255,255)
    elif key == ord("c"):
        canvas = np.ones((650,700,3),np.uint8)*255
    elif key == ord("s"):
        save()
    elif key == ord("+"):
        penSize(1)
    elif key == ord("-"):
        penSize(-1)
    elif key == ord("p"):
        customColor()

cv2.destroyAllWindows()
