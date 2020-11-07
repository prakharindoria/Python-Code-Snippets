from tkinter import *
root=Tk()
root.geometry("733x566")

def myfun():
	print("It works")


menubar=Menu(root)

filemenu=Menu(menubar,tearoff=0)
editmenu=Menu(menubar,tearoff=0)

filemenu.add_command(label="Open",command=myfun)
filemenu.add_command(label="Save",command=myfun)
filemenu.add_command(label="Exit",command=quit)
menubar.add_cascade(label="File",menu=filemenu)


editmenu.add_command(label="Cut",command=myfun)
editmenu.add_command(label="Copy",command=myfun)
menubar.add_cascade(label="Edit",menu=editmenu)






root.config(menu=menubar)




root.mainloop()