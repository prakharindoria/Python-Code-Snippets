from tkinter import *
def changecolor1(e):
    root.configure(bg="yellow")
def changecolor2(e):
    root.configure(bg="orange")
root=Tk()
root.geometry('200x200')
b1=Button(root,text="Click me")
b1.bind("<Button-1>",changecolor1)
b1.bind("<Button-3>",changecolor2)
b1.pack()
root.mainloop()