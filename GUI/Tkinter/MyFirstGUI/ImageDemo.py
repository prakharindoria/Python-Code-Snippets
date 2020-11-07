import tkinter
import tkinter.font
root=tkinter.Tk()
root.title("My gui application")
img=tkinter.PhotoImage(file="D:/kite.png")
myfont=tkinter.font.Font(size=30)
str=tkinter.StringVar()
lbl1=tkinter.Label(root,width=550,height=700,borderwidth=1,relief="sunken",bg="orange",text="   Shadow Fight",compound=tkinter.LEFT,font=myfont)
lbl1.configure(image=img)
root.configure(bg="skyblue")
lbl1.pack()

root.geometry("600x400")
root.mainloop()