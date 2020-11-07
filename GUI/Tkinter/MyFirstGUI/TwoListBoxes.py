from tkinter import *
from tkinter import simpledialog, messagebox
def show_item(e):
    pos = lb1.curselection()
    l1['text']="You selected "+lb1.get(pos[0])
    obj=lb1.get(pos[0])
    lb2.insert(END, obj)



root = Tk()
obj=StringVar()
root.geometry("400x400")
l1 = Label(root, text="Your Selection will appear here")
lb1 = Listbox(root,selectmode=EXTENDED)
lb1.bind("<<ListboxSelect>>",show_item)
lb2 = Listbox(root,selectmode=EXTENDED)
sports = ["Cricket", "Football", "Hockey", "Basketball", "Volleyball", "Tennis", "Rugby", "Badminton"]

for sp in sports:
    lb1.insert(END, sp)

lb1.grid(row=0, column=0, sticky=W)
l1.grid(row=2, column=0, sticky=W)
lb2.grid(row=0, column=4, sticky=W)
root.mainloop()
