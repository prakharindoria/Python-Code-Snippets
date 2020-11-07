from tkinter import *
from datetime import *

def displaymsg():
    today = datetime.now()
    str=today.strftime("%d-%b-%Y %H:%M:%S")
    lbl1.configure(text="Welcome User \n Today is "+str+"\nHappy New Year")
root=Tk()
lbl1=Label(root)
root.geometry("100x200")
b1=Button(root,text="Feeling Lucky ",command=displaymsg)
b1.pack()
lbl1.pack()
root.configure(bg="skyblue")
root.mainloop()


