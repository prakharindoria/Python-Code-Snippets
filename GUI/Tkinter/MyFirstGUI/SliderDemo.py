from tkinter import *
def set_color(val):
     val=sc.get()
     root.configure(bg=('0%s' % hex(val)))




root=Tk()
val=IntVar()
root.geometry("510x510")
sc=Scale(root,from_=0,to=255,orient=HORIZONTAL,command=set_color,length=510,relief =RAISED)
sc.pack()
root.configure(bg="#000")
root.mainloop()
