import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import *
from tkinter import *

win = tk.Tk()
win.resizable(False, False)
win.iconbitmap("Ibah.ico")

val = 0

pb = ttk.Progressbar(win, orient = HORIZONTAL, mode = 'determinate', length = 200)
pb.configure(value = val)

file_name = 'default.txt'

file4 = open(file_name, "r", encoding="utf-8")
file4_data = file4.readlines()

dl1 = file4_data[0]
dl2 = file4_data[1]
dl3 = file4_data[2]
file4.close()

class ChildWindow:
    def __init__(self, parent, width, height, title="Child Window", resizable=(False, False), icon=None):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry("{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)