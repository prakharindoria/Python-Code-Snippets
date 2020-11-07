from tkinter import *

#object of Toolkit
root=Tk()


#function
def getvals():
    if cvalue.get()==0:
        print(username.get())
        print(userpass.get())
    else:
        print(username.get())
        print("********")


#Labels
Label(root,text="Welcome User",font="comicsams 18 bold").grid(row=0,column=1)
Label(root,text="Username").grid(row=1,column=0)
Label(root,text="Password").grid(row=2,column=0)



#EntryVariables
username=StringVar()
userpass=StringVar()
cvalue=IntVar()


#UserInputs
Entry(root,textvariable=username).grid(row=1,column=1)
Entry(root,textvariable=userpass).grid(row=2,column=1)
Checkbutton(root,text="Encrypted",variable=cvalue).grid(row=3,column=1)
Button(root,text="Submit",command=getvals).grid(row=5,column=1)




#run
root.mainloop()