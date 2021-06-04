import tkinter
from os import path
from tkinter import filedialog as fd
from tkinter import *
from tkinter import messagebox
filename = ""

def newfile():  
    t1.delete(0.0, END)

def openfile():
    global filename
    filename = fd.askopenfilename(title = "Select File", filetypes = (("Python Files","*.py"),("Text Files","*.txt"),("All Files","*.*")))
    file = open(filename, "r")
    data = file.readlines()
    t1.delete(0.0, END)
    for line in data:
        t1.insert(END, line)

def helpuser():
    messagebox.showinfo("Help", "[insert help stuff here]")

def helpversion():
    messagebox.showinfo("Version", "The version for this notepad is 1.4.6")

def saveas():
    global filename
    filename = fd.asksaveasfilename(title = "Save File", filetypes=(("Text files", "*.txt"), ("Python file", "*.py"), ("All files", "*.*")))
    data = t1.get(0.0, END)
    file = open(filename, "w")
    for line in data:
        file.write(line)
    file.close()
    messagebox.showinfo("File Success", "File saved successfully!")

def save():
    global filename
    if filename == "":
        saveas()
    else:
        file = open(filename, "w")
        data = t1.get(0.0, END)
        for line in data:
            file.write(line)
        file.close()
        messagebox.showinfo("Success", "File saved successfully!")

def copy():
    window.clipboard_clear()
    data = t1.get("sel.first", "sel.last")
    window.clipboard_append(data)

def paste():
    data = window.selection_get(selection='CLIPBOARD')
    t1.insert('insert', data)

def cut():
    copy()
    t1.delete("sel.first", "sel.last")

window = tkinter.Tk()
window.geometry("500x500+720+200")
window.resizable(0,0)

t1 = Text(window, width = 75, height = 33)
t1.pack()

menubar = Menu(window)

filemenu = Menu(menubar)
filemenu.add_command(label="New", command = newfile)
filemenu.add_command(label="Open", command = openfile)
filemenu.add_command(label="Save", command = save)
filemenu.add_command(label="Save As", command = saveas)
menubar.add_cascade(label="File", menu = filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label="Cut", command = cut)
editmenu.add_command(label="Copy", command = copy)
editmenu.add_command(label="Paste", command = paste)
menubar.add_cascade(label="Edit", menu = editmenu)

helpmenu = Menu(menubar)
helpmenu.add_command(label="Help", command = helpuser)
helpmenu.add_command(label="Version", command = helpversion)
menubar.add_cascade(label="Help", menu = helpmenu)

window.config(menu=menubar)
