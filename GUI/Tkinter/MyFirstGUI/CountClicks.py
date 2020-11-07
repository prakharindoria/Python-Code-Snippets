from tkinter import *
count=0
def incrementcounter():
    count.set(count.get()+1)
root=Tk()
root.geometry('100x200')
count=IntVar()
b1=Button(root,text="Feeling Lucky ",command=incrementcounter)

count=IntVar()
l1=Label(root,textvariable=count)
b1.pack()
l1.pack()
root.mainloop()