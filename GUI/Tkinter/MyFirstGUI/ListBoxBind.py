from tkinter import *
from tkinter import simpledialog, messagebox
def show_item(e):
    pos = lb.curselection()
    l1['text']="You selected "+lb.get(pos[0])



root = Tk()
root.geometry("400x400")
l1 = Label(root, text="Your Selection will appear here")
b1 = Button(root, text="Show Item")
lb = Listbox(root,selectmode=EXTENDED)
lb.bind("<<ListboxSelect>>",show_item)
sports = ["Cricket", "Football", "Hockey", "Basketball", "Volleyball", "Tennis", "Rugby", "Badminton"]

for sp in sports:
    lb.insert(END, sp)

lb.grid(row=0, column=0, sticky=W)
l1.grid(row=2, column=0, sticky=W)
b1.grid(row=1, column=0, sticky=W)
root.mainloop()
