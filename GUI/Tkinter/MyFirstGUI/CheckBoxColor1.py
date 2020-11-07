from tkinter import *


def changecolor():
    root.config(bg=obj.get())


root = Tk()
root.geometry("400x400")
old_color = root["bg"]
obj = StringVar()
cb1 = Checkbutton(root, text="RED", command=changecolor, variable=obj, onvalue="red", offvalue=old_color)
cb1.deselect()
cb1.pack()
root.mainloop()
