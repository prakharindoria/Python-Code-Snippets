from tkinter import *

def fnred():
    l1['bg']="red"

def fngreen():
    l1['bg'] = "green"

def fnblue():
    l1['bg']="blue"



root=Tk()
l1=Label(root,height=3,width=20,bg="white")
b1=Button(root,text="Red",width=6,command=fnred)
b2=Button(root,text="green",width=6,command=fngreen)
b3=Button(root,text="blue",width=6,command=fnblue)

l1.grid(row=0,column=1)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
root.mainloop()