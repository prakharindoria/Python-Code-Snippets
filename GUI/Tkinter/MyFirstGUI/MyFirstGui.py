from tkinter import *
class MyFirstGui:
    def __init__(self,root):
        self.root=root
        self.root.title("An GUI App")
        self.root.geometry('200x200')
        self.label=Label(self.root,text="Click the button")
        self.label.pack()

        self.greet_button=Button(self.root,text="Greet",command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(self.root, text="Close", command=self.root.destroy)
        self.close_button.pack()

    def greet(self):
               self.label.configure(text="Welcome")

root=Tk()
my_gui=MyFirstGui(root)
root.mainloop()