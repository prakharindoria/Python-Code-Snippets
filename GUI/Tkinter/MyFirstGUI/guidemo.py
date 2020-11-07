import tkinter

root=tkinter.Tk()
root.title("My GUI App")
img=tkinter.PhotoImage(file="D:/kite.png")
root.iconphoto(root,img)
"""
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
xco=sh//4
yco=sw//4
height=sh//2
width=sw//2
root.geometry(str(width)+"x"+str(height)+str(xco)+str(yco))#width x height +horizontal +vertical
root.resizable(False,False)
"""
lbl1=tkinter.Label(root,text="Python is a  funny language",fg="white",bg="blue")
lbl2=tkinter.Label(root,text="I was Kidding",fg="white",bg="skyblue")
root.configure(bg="skyblue")
lbl1.pack()
lbl2.pack()
root.mainloop()
