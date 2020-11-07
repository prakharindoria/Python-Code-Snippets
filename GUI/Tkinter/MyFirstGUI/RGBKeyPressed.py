from tkinter import *


def change_color(e):
    if e.char == "r" or e.char == "R":
        root.config(bg="red")
    elif e.char == "g" or e.char == "G":
        root.config(bg="green")
    elif e.char == "b" or e.char == "B":
        root.config(bg="blue")

root = Tk()
root.geometry('200x200')
root.bind("<Key>", change_color)
root.mainloop()
