from tkinter import *


class MyGui:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x400')
        self.b1 = Button(self.root, text="click me", command=self.counter)
        self.lbl = Label(self.root, text="0")
        self.b1.pack()
        self.lbl.pack()
        self.count = 0

    def counter(self):
        self.count += 1
        self.lbl['text'] = str(self.count)


root = Tk()
my_gui = MyGui(root)
root.mainloop()
