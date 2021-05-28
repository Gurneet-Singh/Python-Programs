import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def close():
    answer = messagebox.askyesno("Confirmation", "Are you sure you want to exit Student Form?")
    if answer == True:
        messagebox.showinfo("Message from creator", "Software made by Gurneet Singh.")
        window.destroy()

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    r1.deselect()
    r2.deselect()
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()
    t1.delete(0.0, END)
    

def submit():
    file = open("Studentinfo.txt", "a")
    name = e1.get()
    if name == "" or name == " ":
        messagebox.showerror("Name Error", "Please enter a name")
        return
    else:
        print("Name:", name)

    email = e2.get()
    if email == "" or email == " ":
        messagebox.showerror("Email Error", "Please enter an email")
        return
    elif "@" not in email or "." not in email or email.startswith("@") or email.endswith("@") or email.startswith(".") or email.endswith("."):
        messagebox.showerror("Email Error", "Invalid email")
        return
    else:
        print("Email:", email)

    gendervalue = v.get()
    if gendervalue == 0:
        messagebox.showerror("Gender Error", "Please select a gender")
        return
    else:
        if gendervalue == 1:
            print("Gender: Male")
        if gendervalue == 2:
            print("Gender: Female")

    transport = []
    cyclevalue = int(v1.get())
    walkvalue = int(v2.get())
    busvalue = int(v3.get())
    carvalue = int(v4.get())
    othervalue = int(v5.get())
    totaltransport = cyclevalue + walkvalue + busvalue + carvalue + othervalue
    if totaltransport == 0:
        messagebox.showerror("Checkbox Error", "Please select a checkbox")
        return
    else:
        if cyclevalue == 1:
            transport.append("bicycle")
        if walkvalue == 1:
            transport.append("walk")
        if busvalue == 1:
            transport.append("bus")
        if carvalue == 1:
            transport.append("car")
        if othervalue == 1:
            other = e3.get()
            if other == "" or other == " ":
                messagebox.showerror("Entry Error", "Please enter your other use of transportation")
                return
            else:
                transport.append(other)
        print(transport)
    address = t1.get(0.0, END)
    address = address.rstrip("\n")
    if address == "" or address == " ":
        messagebox.showerror("Textbox Error", "Please enter an address")
        return
    else:
        print("Address:", address)

    subjectvalue = Lb1.curselection()
    if len(subjectvalue) == 0:
        messagebox.showerror("Select Error", "Please select a favorite subect")
        return
    else:
        subjects = ["Language Arts", "Social Studies", "Science", "Math", "P.E"]
        print(subjects[subjectvalue[0]])
        favsubject = subjects[subjectvalue[0]]

    age = Sp1.get()
    print("Age:", age)

    grade = cb1.get()
    file.write("Name: " + name + "\n")
    file.write("Email: " + email + "\n")
    if gendervalue == 1:
        file.write("Gender: Male" + "\n")
    if gendervalue == 2:
        file.write("Gender: Female" + "\n")
    for vehicle in transport:
        file.write("Transportation: " + vehicle + "\n")
    file.write("Address: " + address + "\n")
    file.write("Favorite Subject: " + favsubject + "\n")
    file.write("Age: " + age + "\n")
    file.write("Grade: " + grade + "\n\n\n")
    file.close()
    messagebox.showinfo("Information", "Successfully added information into the file :)")

window = tkinter.Tk()
window.geometry("750x750+750+200")
window.resizable(0,0)
window.title("Form")

lab1 = Label(window, text = "STUDENT ENTRY FORM", fg = "black", font = "Times 15 bold")
lab1.grid(row = 0, column = 1)

lab2 = Label(window, text = "NAME", fg = "black", font = "Times 10 bold")
lab2.grid(row = 1, column = 0)
e1 = Entry(window, width = 45)
e1.grid(row = 1, column = 1)

lab3 = Label(window, text = "EMAIL", fg = "black", font = "Times 10 bold")
lab3.grid(row = 2, column = 0)
e2 = Entry(window, width = 45)
e2.grid(row = 2, column = 1)

lab4 = Label(window, text = "GENDER", font = "Times 10 bold")
lab4.grid(row = 3, column = 0)

v = IntVar()
r1 = Radiobutton(window, text = "Male", variable = v, value = 1, font = "Times 10 bold")
r1.grid(row = 3, column = 1)

r2 = Radiobutton(window, text = "Female", variable = v, value = 2, font = "Times 10 bold")
r2.grid(row = 3, column = 2)

lab5 = Label(window, text = "VEHICLE", font = "Times 10 bold")
lab5.grid(row = 4, column = 0)

v1 = IntVar()
c1 = Checkbutton(window, text = "Bicycle", variable = v1, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c1.grid(row = 4, column = 1)

v2 = IntVar()
c2 = Checkbutton(window, text = "Walk", variable = v2, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c2.grid(row = 4, column = 2)

v3 = IntVar()
c3 = Checkbutton(window, text = "Bus", variable = v3, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c3.grid(row = 5, column = 1)

v4 = IntVar()
c4 = Checkbutton(window, text = "Car", variable = v4, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c4.grid(row = 5, column = 2)

v5 = IntVar()
c5 = Checkbutton(window, text = "Other", variable = v5, onvalue = 1, offvalue = 0, font = "Times 10 bold")
c5.grid(row = 6, column = 1)

e3 = Entry(window, width = 15)
e3.grid(row = 6, column = 2)

lab6 = Label(window, text = "ADDRESS", font = "Times 10 bold")
lab6.grid(row = 7, column = 0)
t1 = Text(window, width = 20, height = 3)
t1.grid(row = 7, column = 1)

lab7 = Label(window, text = "FAVORITE SUBJECT", font = "Times 10 bold")
lab7.grid(row = 8, column = 0)

Lb1 = Listbox(window, width = 15, height = 5, selectmode = "multiple")
Lb1.insert(0, "P.E")
Lb1.insert(0, "Math")
Lb1.insert(0, "Science")
Lb1.insert(0, "Social Studies")
Lb1.insert(0, "Language Arts")
Lb1.grid(row = 8, column = 1)

lab8 = Label(window, text = "AGE", font = "Times 10 bold")
lab8.grid(row = 9, column = 0)
Sp1 = Spinbox(window, from_=10, to=13)
Sp1.grid(row = 9, column = 1)

lab9 = Label(window, text = "GRADE", font = "Times 10 bold")
lab9.grid(row = 10, column = 0)
n = StringVar()
cb1 = ttk.Combobox(window, width = 27, textvariable = n)
cb1['values'] = ("6th grade", "7th grade", "8th grade")
cb1.grid(row = 10, column = 1)

b1 = Button(window, text = "CLEAR", font = "Times 10 bold", command = clear)
b1.grid(row = 11, column = 0, pady = 25)
b2 = Button(window, text = "SUBMIT", font = "Times 10 bold", command = submit)
b2.grid(row = 11, column = 1, pady = 25)
b3 = Button(window, text = "EXIT", font = "Times 10 bold", command = close)
b3.grid(row = 11, column = 2, pady = 25)
