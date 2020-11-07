from tkinter import *
def finish():
    root.destroy()
def show():
    fname=e1.get()
    lname=e2.get()
    l3.config(text=fname+" "+lname)

root=Tk()
l1=Label(root,text="First Name")
l2=Label(root,text="Last Name")
l3=Label(root,width=20,anchor=W,font="Arial 10 bold")
e1=Entry(root)
e2=Entry(root)
b1=Button(root,text='Show',command=show)
b2=Button(root,text="Quit",command=finish)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=2,column=0)
e2.grid(row=2,column=1)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
l3.grid(row=4,column=1)
root.mainloop()

