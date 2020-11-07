from tkinter import *
from tkinter import messagebox, simpledialog


def accept():
    num=simpledialog.askinteger("Input","age",minvalue=18,maxvalue=122)
    messagebox.showinfo("Hello", "You entered Age"+str(num))

root=Tk()
root.geometry()
btn=Button(root,text="CLick me",command=accept)
btn.pack()
root.mainloop()