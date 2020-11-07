#Layouting :pack(),grid(),place()
import tkinter
import tkinter.font
root=tkinter.Tk()
root.geometry('200x200+100+200')
root.title("My gui application")
lbl1=tkinter.Label(root,text="Red Sun",bg="red",fg="black")
lbl2=tkinter.Label(root,text="Blue Sky",bg="blue",fg="white")
lbl3=tkinter.Label(root,text="Green Grass",bg="Green",fg="black")
lbl4=tkinter.Label(root,text="Brown Crust",bg="Brown",fg="white")
lbl1.grid(row=0,column=0,padx=5)
lbl2.grid(row=1,column=1,padx=5)
lbl3.grid(row=2,column=2,padx=5)
lbl4.grid(row=3,column=3,padx=5)

root.configure(bg="skyblue")

root.mainloop()