from tkinter import *
from tkinter import colorchooser, messagebox


def showopen():
    c=colorchooser.askcolor(title="Choose Color",color="red")
    if type(c[0]) is tuple:
        root.config(bg=c[1])
    else:
        messagebox.showinfo("No Color Choosen", "Please choose a color")

root=Tk()
root.geometry("400x400")
btn=Button(root,text="Choose Color",command=showopen)
btn.pack()
root.mainloop()