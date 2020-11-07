from tkinter import *
from tkinter import messagebox
def showgender():
    num=obj.get()
    if num==1:
        messagebox.showinfo("Selection", "You selected Male")


    else:
        messagebox.showinfo("Selection", "You selected Female")


root=Tk()
root.geometry("200x200")
obj = IntVar()
l1=Label(root,text="Select Your Gender")
rb1=Radiobutton(root,text="Male",command=showgender,variable=obj,value=1)
rb2=Radiobutton(root,text="Female",command=showgender,variable=obj,value=2)
l1.grid(row=0,column=0)
rb1.grid(row=1,column=0,sticky=W)
rb2.grid(row=2,column=0,sticky=W)
root.mainloop()