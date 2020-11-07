from tkinter import *
def changecolor(e):
    root.config(bg="red")

def retaincolor(e):
    root.config(bg=oldcolor)

root=Tk()
root.geometry('200x200')
oldcolor=root["bg"]
root.bind("j",changecolor)

root.bind("n",retaincolor)


root.mainloop()