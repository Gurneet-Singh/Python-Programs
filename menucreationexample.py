import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.geometry("500x500+720+200")
window.resizable(0,0)
menubar = Menu(window)
menu1 = Menu(menubar)
menu1.add_command(label="Menu Item1")
menu1.add_command(label="Menu Item2")
menubar.add_cascade(label="Menu1", menu = menu1)
menu2 = Menu(menubar)
menu2.add_command(label="Menu Item1")
menu2.add_command(label="Menu Item2")
menubar.add_cascade(label="Menu2", menu = menu2)
window.config(menu=menubar)
