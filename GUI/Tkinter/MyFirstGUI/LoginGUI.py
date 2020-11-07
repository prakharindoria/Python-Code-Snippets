import tkinter.font

root = tkinter.Tk()
root.title("My gui application")
lbl1 = tkinter.Label(root, text="Name:")
lbl2 = tkinter.Label(root, text="Password:")
e1 = tkinter.Entry(root)
e2 = tkinter.Entry(root)
b1 = tkinter.Button(root, text="Login")
b2 = tkinter.Button(root, text="Quit")
c1 = tkinter.Checkbutton(root, text="Keep me logged in")
lbl1.grid(row=0, column=0, sticky=tkinter.E)  # compass alignment like n e w s ne ....
lbl2.grid(row=1, column=0)
e1.grid(row=0, column=1, columnspan=2)
c1.grid(row=2, column=2, columnspan=2)
e2.grid(row=1, column=1)
b1.grid(row=2, column=0, sticky=tkinter.W + tkinter.E)
b2.grid(row=2, column=1, sticky=tkinter.W + tkinter.E)
root.mainloop()
