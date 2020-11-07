from tkinter import *
from tkinter import messagebox, simpledialog


class MyGui:
    def __init__(self, root):
        self.root = root
        self.root.geometry("250x200+100+200")
        self.l1 = Label(root, text="Number Division Program", font="Arial 15", width=20, anchor=W)
        self.l2 = Label(root, text="Enter First no.", width=10, anchor=W)
        self.l3 = Label(root, text="Enter Second no.", width=10, anchor=W)
        self.l4 = Label(root, text="Result", width=10, anchor=W)
        self.b1 = Button(root, text="Divide", command=self.divide)
        self.b2 = Button(root, text="Clear", command=self.clear)
        self.b3 = Button(root, text="Quit", command=self.finish)
        self.e1 = Entry(root)
        self.e2 = Entry(root)
        self.e3 = Entry(root)
        self.l1.grid(row=0, column=0, columnspan=4)
        self.l2.grid(row=1, column=0)
        self.l3.grid(row=2, column=0)
        self.l4.grid(row=3, column=0)
        self.b1.grid(row=4, column=0)
        self.b2.grid(row=4, column=1)
        self.b3.grid(row=4, column=2)
        self.e1.grid(row=1, column=2)
        self.e2.grid(row=2, column=2)
        self.e3.grid(row=3, column=2)

    def divide(self):
        try:
            self.e3.delete(0, END)
            self.e3.config(fg="red")
            a = int(self.e1.get())
            b = int(self.e2.get())
            c = a / b
            self.e3.insert(0, str(c))
            self.e3.config(fg="green")

        except ZeroDivisionError:

            self.e3.insert(0,"Cant divide by Zero")
            messagebox.showerror("Invalid Number", "Please input non zero denominator")

        except ValueError:
            self.e3.insert(0, "Please input digits only")
            messagebox.showerror("Error", "Please enter digits only")

    def clear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e1.focus()

    def finish(self):
        ans=messagebox.askyesno("Quitting","Are you sure?")
        if ans==True:
            name=simpledialog.askstring("Name","What is your name")
            if name=="" or name is None:
                name="User"

            messagebox.showinfo("Bye","Have a good day "+name)
            self.root.destroy()


root = Tk()
obj = MyGui(root)
root.mainloop()
