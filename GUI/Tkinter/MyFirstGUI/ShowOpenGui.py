from tkinter import *
from tkinter import filedialog,messagebox

def showbox():
    files=filedialog.askopenfilenames(filetypes=[("Movies",".mp4")],title="Selesct Your Favorite Movies")
    str=""
    if type(files) is tuple:
        for f in files:
            str+=f+"\n"
    else:
        str="You did not selected any file"
    lbl.config(text=str)




root= Tk()
root.geometry("400x400")
lbl=Label(root,text=" ")
button=Button(root,text="CLick",command=showbox)
button.pack()
lbl.pack()
root.mainloop()

