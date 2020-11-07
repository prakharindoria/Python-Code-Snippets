from tkinter import *
root=Tk()
root.geometry("200x200")
lb=Listbox()
sports=["Cricket","Football","Hockey","Basketball","Volleyball"]
for sp in sports:
    lb.insert(END,sp)
print(lb.size())
print(lb.get(0))#returns a string
print(lb.get(0,3))#returns a tuple
lb.delete(2)#deletes at position

lb.grid(row=1,column=0,sticky=W)
root.mainloop()
