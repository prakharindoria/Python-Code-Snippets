import tkinter
import tkinter.font
root=tkinter.Tk()
root.title("My gui application")
myfont=tkinter.font.Font(size=20)
img=tkinter.PhotoImage(file="D:/kite.png")
lbl1=tkinter.Label(root,text="Python Rocks",font=myfont,width=50,height=4,borderwidth=1,relief="sunken",bg="orange",image=img)

root.configure(bg="skyblue")
lbl1.pack()

root.geometry("600x400")
root.mainloop()
