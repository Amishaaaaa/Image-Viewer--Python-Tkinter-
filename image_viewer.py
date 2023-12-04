from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os

def showimage():
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image file",
        filetypes=(("JPG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
    )
    if filename:
        img = Image.open(filename)
        lbl.config(text="")
        w, h = img.size
        ratio_w = 400 / w
        ratio_h = 400 / h
        ratio = min(ratio_w, ratio_h)
        new_w = int(w * ratio)
        new_h = int(h * ratio)
        img = img.resize((new_w, new_h), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img)
        lbl.image = img

root = Tk()

lbl = Label(root)
lbl.pack(fill=BOTH, expand=YES)

fram = Frame(root)
fram.pack(side=BOTTOM, padx=15, pady=15)

btn = Button(fram, text="Select Image", command=showimage)
btn.pack(side=tk.LEFT)

btn2 = Button(fram, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=12)

root.title("Image Viewer")
root.geometry("400x450")
root.mainloop()
