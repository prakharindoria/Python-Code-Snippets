from tkinter import *
from tkinter import messagebox, simpledialog
def divide():
    try:
        e3.delete(0,END)
        a=int(e1.get())
        b=int(e2.get())
        c=a/b
        e3.insert(0,str(c))

    except ZeroDivisionError:
        messagebox.showinfo("Invalid Number", "Can't divide by Zero")

    except ValueError:
        messagebox.showinfo("Digits only", "Plaese enter valid digits")

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


def finish():
    ans = messagebox.askyesno("Quitting", "Are you sure you want to Quit?")
    if ans == True:
        name = simpledialog.askstring("Input", "Input Your Name")
        if name is None or name == "":
            name = "UserJee"
        messagebox.showinfo("Thanks", "Good day " + name + "!")
        root.destroy()


root = Tk()
root.geometry("250x200+100+200")
l1 = Label(root, text="Number Division Program", font="Arial", width=20, anchor=W)
l2 = Label(root, text="Enter First no.", width=10, anchor=W)
l3 = Label(root, text="Enter Second no.", width=10, anchor=W)
l4 = Label(root, text="Result", width=10, anchor=W)
b1 = Button(root, text="Divide", command=divide)
b2 = Button(root, text="Clear", command=clear)
b3 = Button(root, text="Quit", command=finish)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
l1.grid(row=0, column=0, columnspan=4)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)
b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
e1.grid(row=1, column=2)
e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
root.mainloop()
