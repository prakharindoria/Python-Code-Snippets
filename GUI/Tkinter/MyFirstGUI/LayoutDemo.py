#Layouting :pack(),grid(),place()
import tkinter
import tkinter.font
root=tkinter.Tk()
root.title("My gui application")
lbl1=tkinter.Label(root,text="Red Sun",bg="red",fg="black")
lbl2=tkinter.Label(root,text="Blue Sky",bg="blue",fg="white")
lbl3=tkinter.Label(root,text="Green Grass",bg="Green",fg="black")
lbl4=tkinter.Label(root,text="Brown Crust",bg="Brown",fg="white")
lbl5=tkinter.Label(root,text="Yellow Core",bg="Yellow",fg="black")

root.configure(bg="skyblue")
lbl1.pack(fill=tkinter.X,padx=(300,300),pady=1,ipady=60)
lbl2.pack(fill=tkinter.X,padx=(300,300),ipady=60)
lbl3.pack(fill=tkinter.X,padx=(300,300),ipady=60)
lbl4.pack(fill=tkinter.X,padx=(300,300),ipady=60)
lbl5.pack(fill=tkinter.X,padx=(300,300),ipady=60)

root.mainloop()