from tkinter import *


def changecolor():
    if obj1.get() == 1:
        root.config(bg="#ff0000")

    elif obj2.get() == 1:
        root.config(bg="green")

    elif obj3.get()==1:
        root.config(bg="blue")

    else:
        root.config(bg=old_color)
    if obj1.get() == 1 and obj2.get() == 1:
        root.config(bg="#ffff00")
    elif obj2.get() == 1 and obj3.get() == 1:
        root.config(bg="#00ffff")
    elif obj1.get() == 1 and obj3.get() == 1:
        root.config(bg="#ff00ff")

    if obj1.get() == 1 and obj2.get() == 1 and obj3.get()==1:
        root.config(bg="#ffffff")


root = Tk()
root.geometry("500x500")
old_color = root["bg"]
obj1 = IntVar()
obj2 = IntVar()
obj3 = IntVar()
cb1 = Checkbutton(root, text=" Red   ", command=changecolor, variable=obj1)
cb2 = Checkbutton(root, text="Green", command=changecolor, variable=obj2)
cb3 = Checkbutton(root, text=" Blue  ", command=changecolor, variable=obj3)
cb1.pack(side=TOP)
cb2.pack(side=TOP)
cb3.pack(side=TOP)
root.mainloop()
