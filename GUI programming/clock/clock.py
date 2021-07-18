from tkinter import *
from tkinter.ttk import *

from time import strftime

import sys

root = Tk()
root.title("Clock")
root.resizable(False, False)
root.geometry("440x140")


# sys.setrecursionlimit(10000)


def time():
    string_time = strftime('%I:%M:%S')
    label.config(text=string_time)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 100), background="black", foreground="green", relief=RAISED, width=400)
label.pack(anchor='c')

time()

mainloop()
