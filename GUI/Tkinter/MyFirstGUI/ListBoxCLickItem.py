from tkinter import *
from tkinter import simpledialog, messagebox


def show_item():
    pos = lb.curselection()
    if len(pos) == 0:
        messagebox.showerror("Error", "Please select an item")
    else:
        str=""
        for i in pos:
            str+= lb.get(i)+"\n"
            l1['text'] = "You Selected:\n" +str


root = Tk()
root.geometry("400x400")
l1 = Label(root, text="Your Selection will appear here")
b1 = Button(root, text="Show Item", command=show_item)
lb = Listbox(root,selectmode=EXTENDED)
sports = ["Cricket", "Football", "Hockey", "Basketball", "Volleyball", "Tennis", "Rugby", "Badminton"]

for sp in sports:
    lb.insert(END, sp)

lb.grid(row=0, column=0, sticky=W)
l1.grid(row=2, column=0, sticky=W)
b1.grid(row=1, column=0, sticky=W)
root.mainloop()
