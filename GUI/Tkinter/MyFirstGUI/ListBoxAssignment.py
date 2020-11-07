from tkinter import *
from tkinter import simpledialog,messagebox
def show_item():
    pos=simpledialog.askinteger("Input","Enter Position",minvalue=1,maxvalue=lb.size())
    if type(pos) is int:
        item=lb.get(pos-1)
        l1.config(text="You seleted "+item,bg="skyblue")
        root.config(bg="Skyblue")
    else:
        l1['text']="You did not input an item no"


root=Tk()
root.geometry("400x400")
l1=Label(root,text="Your Selection will appear here")
b1=Button(root,text="Show Item",command=show_item)
lb=Listbox()
sports=["Cricket","Football","Hockey","Basketball","Volleyball","Tennis","Rugby","Badminton"]

for sp in sports:
    lb.insert(END,sp)


lb.grid(row=0,column=0,sticky=W)
l1.grid(row=2,column=0,sticky=W)
b1.grid(row=1,column=0,sticky=W)
root.mainloop()
