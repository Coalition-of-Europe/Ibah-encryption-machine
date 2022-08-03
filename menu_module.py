import tkinter as tk
import tkinter.messagebox as mes
import tkinter.filedialog as fil
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from win import ChildWindow as cw
from win import *
from time import sleep

wanted_files = [("Text files", "*.txt")]

val2 = 0

class ExetWindow:
    def exet(parent=Toplevel):
        choice = mes.askyesno("Exit", message="Do you want to exit?", icon="warning")
        if choice:
            parent.destroy(win) 

def upload_a_set():
    file_name = fil.askopenfilename(filetypes = wanted_files)
    if file_name:
        file4 = open(file_name, "r", encoding="utf-8")
        let_rus.clear()
        let_eng.clear()
        let_eng_big.clear()
        pb = ttk.Progressbar(win, orient = HORIZONTAL, mode = 'determinate', length = 200)
        pb.configure(value = val)
        pb.grid(row = 2, column = 1)
        for l in range(0, len(dl1)-1):
            let_rus.append(file4.readline(1))
            val2 = l
            pb.configure(value = val2)
            pb.update()
            sleep(0.01)
        for l2 in range(0, len(dl2)):
            let_eng.append(file4.readline(1))
            val2 = val2+l2
            pb.configure(value = val2)
            pb.update()
            sleep(0.01)
        let_eng.pop(0)
        for l3 in range(0, len(dl3)):
            let_eng_big.append(file4.readline(1))
            val2 = val2+l3
            pb.configure(value = val2)
            pb.update()
            sleep(0.01)
        let_eng_big.pop(0)
        file4.close()
        val2 = 100
        pb.configure(value = val2)
        pb.update()
        val2 = 0
        pb.configure(value = val2)
        pb.update()
        pb.destroy()

def reset_set():
    file_name = "default.txt"

let_rus = []
let_eng = []
let_eng_big = []

