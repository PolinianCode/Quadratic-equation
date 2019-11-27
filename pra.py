from tkinter import *
import math

#Descriminant function

def find_d():
    #b^2-4ac
    global d
    d = int(b_var.get())**2 - 4*int(a_var.get())*int(c_var.get())
    check_d()

def type_check():
    find_d()


def check_d():
    if d > 0:
        x1_value = (-int(b_var.get()) + math.sqrt(d))/ (2*int(a_var.get()))
        x1_data.set(x1_value)

        x2_value = (-int(b_var.get()) - math.sqrt(d))/ (2*int(a_var.get()))
        x2_data.set(x2_value)
        l.config(text = "")
    elif d == 0:
        x1_value = (-int(b_var.get()) + math.sqrt(d))/ (2*int(a_var.get()))
        x1_data.set(x1_value)
        x2_data.set(x1_value)
        l.config(text = "")
    else:
        l.config(text = "Нету корней в данном уравнении")


def main_window():
    #Creating Window
    global screen
    screen = Tk()
    screen.title("New Window")
    screen.geometry("300x300")

    #global variables
    global a_var
    global b_var
    global c_var

    global a_entry
    global b_entry
    global c_entry

    global x1_data
    global x2_data

    global l

    #Setting variables type

    a_var = StringVar()
    b_var = StringVar()
    c_var = StringVar()


    x1_data = StringVar()
    x2_data = StringVar()


    #The fields for a,b and c
    Label(screen , text="A:").pack()
    a_entry = Entry(screen, textvariable=a_var)
    a_entry.pack()



    Label(screen , text="B:").pack()
    b_entry = Entry(screen, textvariable=b_var)
    b_entry.pack()



    Label(screen , text="C:").pack()
    c_entry = Entry(screen, textvariable=c_var)
    c_entry.pack()



    #Spaces
    l = Label(screen, text="")
    l.pack()
    Label(screen, text="").pack()

    #Buttons
    Button(text = "Calculate", command=type_check).pack()
    Label(screen, text="").pack()


    #The x values

    Label(screen, text="X1:").pack()

    x1 = Entry(screen, textvariable=x1_data)
    x1.pack()
    Label(screen, text="X2:").pack()
    x2 = Entry(screen, textvariable=x2_data)
    x2.pack()
    screen.mainloop()



main_window()
