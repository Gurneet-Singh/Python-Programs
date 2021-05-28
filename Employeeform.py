import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    r1.deselect()
    r2.deselect()
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()
    c6.deselect()
    c7.deselect()

def close():
    answer = messagebox.askyesno("Confirmation", "Are you sure you want to exit Employee Form?")
    if answer == True:
        messagebox.showinfo("Message from creator", "Software made by Gurneet Singh.")
        window.destroy()

def submit():
    name = e1.get()
    if name == "":
        messagebox.showerror("Name Error", "Please eneter a name")
        return
    else:
        print("Name:", name)

    age = e2.get()
    if age == "":
        messagebox.showerror("Age Error", "Please enter an age")
        return
    else:
        print("Age:", age)

    gendervalue = v.get()
    if gendervalue == 0:
        messagebox.showerror("Gender Error", "Please select a gender")
        return
    else:
        if gendervalue == 1:
            print("Gender: Male")
        if gendervalue  == 2:
            print("Gender: Female")

    days = []
    s = int(v1.get())
    m = int(v2.get())
    t = int(v3.get())
    w = int(v4.get())
    th = int(v5.get())
    f = int(v6.get())
    sa = int(v7.get())
    totaldays = s + m + t + w + th + f + sa
    if totaldays == 0:
        messagebox.showerror("Checkbox Error", "Please select a checkbox")
        return
    else:
        if s == 1:
            days.append("sunday")
        if m == 1:
            days.append("monday")
        if t == 1:
            days.append("tuesday")
        if w == 1:
            days.append("wednesday")
        if th == 1:
            days.append("thrusday")
        if f == 1:
            days.append("friday")
        if sa == 1:
            days.append("saturday")
            
        print(totaldays)

window = tkinter.Tk()
window.geometry("500x400+750+200")
window.resizable(0,0)
window.title("Form")

lab1 = Label(window, text = "EMPLOYEE ENTRY FORM", fg = "black", font = "Times 15 bold")
lab1.grid(row = 0, column = 1)

lab2 = Label(window, text = "NAME", fg = "black", font = "Times 10 bold")
lab2.grid(row = 1, column = 0)
e1 = Entry(window, width = 15)
e1.grid(row = 1, column = 1)

lab3 = Label(window, text = "AGE", fg = "black", font = "Times 10 bold")
lab3.grid(row = 2, column = 0)
e2 = Entry(window, width = 15)
e2.grid(row = 2, column = 1)

lab4 = Label(window, text = "GENDER", font = "Times 10 bold")
lab4.grid(row = 3, column = 0)

v = IntVar()
r1 = Radiobutton(window, text = "Male", variable = v, value = 1, font = "Times 10 bold")
r1.grid(row = 3, column = 1)

r2 = Radiobutton(window, text = "Female", variable = v, value = 2, font = "Times 10 bold")
r2.grid(row = 3, column = 2)

lab5 = Label(window, text = "WORK AS...", font = "Times 10 bold")
lab5.grid(row = 4, column = 0)

n = StringVar()
cb1 = ttk.Combobox(window, width = 15, textvariable = n)
cb1['values'] = ("Worker", "Manager", "Janitor")
cb1.grid(row = 4, column = 1)

lab5 = Label(window, text = "DAYS YOU CAN WORK", font = "Times 10 bold")
lab5.grid(row = 5, column = 0)

v1 = IntVar()
c1 = Checkbutton(window, text = "S", variable = v1, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c1.grid(row = 5, column = 1)

v2 = IntVar()
c2 = Checkbutton(window, text = "M", variable = v2, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c2.grid(row = 5, column = 2)

v3 = IntVar()
c3 = Checkbutton(window, text = "T", variable = v3, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c3.grid(row = 5, column = 3)

v4 = IntVar()
c4 = Checkbutton(window, text = "W", variable = v4, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c4.grid(row = 6, column = 1)

v5 = IntVar()
c5 = Checkbutton(window, text = "Th", variable = v5, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c5.grid(row = 6, column = 2)

v6 = IntVar()
c6 = Checkbutton(window, text = "F", variable = v6, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c6.grid(row = 6, column = 3)

v7 = IntVar()
c7 = Checkbutton(window, text = "Sa", variable = v7, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c7.grid(row = 7, column = 1)

b1 = Button(window, text = "CLEAR", font = "Times 10 bold", command = clear)
b1.grid(row = 8, column = 0, pady = 25)
b2 = Button(window, text = "SUBMIT", font = "Times 10 bold", command = submit)
b2.grid(row = 8, column = 1, pady = 25)
b3 = Button(window, text = "EXIT", font = "Times 10 bold", command = close)
b3.grid(row = 8, column = 2, pady = 25)
