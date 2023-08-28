import tkinter as tk
from tkinter.filedialog import *
import os
try:
    import pyautogui
except ImportError:
    os.system('pip install pyautogui')
    import pyautogui
root = tk.Tk()
canvas1 = tk.Canvas(root, height=300, width=300)
canvas1.pack()

def takescreenshot():
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename(defaultextension=".png")
    if save_path:
        myscreenshot.save(save_path)
        
myButton = tk.Button(text="Take Screenshot", command=takescreenshot, font=10)
canvas1.create_window(150, 150, window=myButton)

tk.mainloop()
