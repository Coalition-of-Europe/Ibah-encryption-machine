import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as sc
from menu_module import ExetWindow as ew
from tkinter import *
from alpha import *
from menu_module import *
from tkinter.scrolledtext import *
from tkinter.filedialog import *
from tkinter.ttk import Progressbar
from tkinter.ttk import *
from win import *
from win import ChildWindow as cw
from win import file_name
from time import sleep

file = open("last_log.txt", "w")
file2 = open("sym.txt", "r", encoding="utf-8")

file4 = open(file_name, "r", encoding="utf-8")

def upl():
    pb.grid(row = 2, column = 1)
    for l in range(0, len(dl1)-1):
        let_rus.append(file4.readline(1))
        val = l
        pb.configure(value = val)
        pb.update()
        sleep(0.01)
    for l2 in range(0, len(dl2)):
        let_eng.append(file4.readline(1))
        val = val+l2
        pb.configure(value = val)
        pb.update()
        sleep(0.01)
    let_eng.pop(0)
    for l3 in range(0, len(dl3)):
        let_eng_big.append(file4.readline(1))
        val = val+l3
        pb.configure(value = val)
        pb.update()
        sleep(0.01)
    let_eng_big.pop(0)
    file4.close()
    val = 100
    pb.configure(value = val)
    pb.update()
    val = 0
    pb.configure(value = val)
    pb.update()
    pb.destroy()

t3 = file2.readlines()
eng_sym = []
rus_sym = []
for sym3 in range(0, 3):
    eng_sym.append(t3[sym3])
for sym2 in range(1, 4):
    rus_sym.append(t3[sym2+3])
file2.close()

file3 = open("Language.txt", "r", encoding="utf-8")
t1 = file3.readlines()
file3.close()

win.resizable(width=None, height=None)
win.title("Ibah")

win.grid_columnconfigure(0, minsize=10)
win.grid_columnconfigure(1, minsize=10)

te1 = tk.Label(win, text=(t1[1]), font=('Times New Roman', 14))
te1.grid(row=1, column=0, stick='e')
te2 = tk.Label(win, text=(t1[0]), font=('Times New Roman', 14))
te2.grid(row=0, column=0, stick='e')
te3 = tk.Label(win, text=(''.join(eng_sym)), font=('Times New Roman', 14))
te3.grid(row=1, column=2)

en=sc.ScrolledText(win, font=('Times New Roman', 14), width=20, height=5, wrap = WORD)
en.grid(row=0, column=1)

menu_bar=Menu(win)
win.configure(menu=menu_bar)

b=[]
itog=""

def rus():
    file3 = open("Language.txt", "r+", encoding="utf-8")
    file2 = open("sym.txt", "r", encoding="utf-8")
    t1[13] = "rus"
    file3.write(''.join(t1))
    te1.configure(text=t1[6])
    te2.configure(text=t1[7])
    te3.configure(text=''.join(rus_sym))
    bu1.configure(text=t1[10])
#    me1.configure(label=t1[8])
#    me2.configure(label=t1[9])    
    file3.close()
    file2.close()

def eng():
    file3 = open("Language.txt", "r+", encoding="utf-8")
    file2 = open("sym.txt", "r", encoding="utf-8")
    t1[13] = "eng"
    file3.write(''.join(t1))
    te1.configure(text=t1[0])
    te2.configure(text=t1[1])
    te3.configure(text=''.join(eng_sym))
    bu1.configure(text=t1[4])
#    me1.configure(label=t1[2])
#    me2.configure(label=t1[3])
    file3.close()
    file2.close()

def shifr():
    file = open("last_log.txt", "a")
    file.write("\nIntroduced: ")
    file.write(en.get("1.0", END))
    file4 = open(file_name, "r", encoding="utf-8")
    sh = en.get("1.0", END)
    te.delete("1.0", END)

    for i in range(0, len(sh)):
            for g in range(0, len(let_rus)):
                if sh[i]==let_rus[g]:
                    b.append(let_eng[g])
                elif sh[i]==let_eng[g]:
                    b.append(let_rus[g])

            for g2 in range(0, len(let_rus)-len(let_eng_big)):
                if sh[i]==((''.join(let_rus[g2])).upper()):
                    b.append((''.join(let_eng[g2])).upper())
                elif sh[i]==((''.join(let_eng[g2])).upper()):
                    b.append((''.join(let_rus[g2])).upper())

            for g3 in range(len(let_rus)-len(let_eng_big), len(let_rus)):
                    if sh[i]==((let_rus[g3]).upper()):
                        b.append(let_eng_big[len(let_rus)-g3-1])
                    elif sh[i]==(let_eng_big[len(let_rus)-g3-1]):
                        b.append((let_rus[g3]).upper())

            for s in range(0, len(sym)):
                if sh[i]==sym[s]:
                    b.append(sym[s])

            for z in range(0, 10):
                if sh[i]==zahl[z]:
                    b.append(zahl[z])
                    
    itog = "".join(b)
    file.write("Output: ")
    file.write(itog)
    file.write('\n')
    file.close()
    file4.close()
    b.clear()
    te.insert("1.0", itog)  

file_menu = Menu(menu_bar, tearoff=0)
me1 = file_menu.add_command(label=(t1[2]), command=upload_a_set)
me2 = file_menu.add_command(label=(t1[3]), command=reset_set)

language_menu = Menu(menu_bar, tearoff=0)
language_menu.add_command(label="English", command=eng)
language_menu.add_command(label="Russian", command=rus)

menu_bar.add_cascade(label="Language", menu=language_menu)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_command(label="Quit", command=ew.exet)

bu1 = tk.Button(win, text=(t1[4]), command = (shifr), font=('Times New Roman', 14))
bu1.grid(row=0, column=2)

#button = tk.Button()
#button.bind("<Insert>", paste_buff)

if t1[13] == 'rus':
    rus()
if t1[13] == 'eng':
    eng()

te = sc.ScrolledText(win, font=('Times New Roman', 14), width=20, height=5, wrap = WORD)
te.grid(row=1, column=1)

upl()

tk.mainloop()

#pyinstaller -w -F -i "C:\Users\Даниил Ситников\Desktop\Ibah\Ibah.ico" Ibah.py

