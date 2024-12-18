
from tkinter import *
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")
def labelss():

    name_label1 = Label(windows,text="File",fg="blue",bg="white",font=("Jokerman",10,"bold","underline"),justify="center")
    name_label2 = Label(windows,text="Edit",fg="blue",bg="white",font=("Jokerman",10,"bold","underline"))
    name_label3 = Label(windows,text="View",fg="blue",bg="white",font=("Jokerman",10,"bold","underline"))

    name_label1.place(x=0,y=0)
    name_label2.place(x=50,y=0)
    name_label3.place(x=100,y=0)

name_btn = Button(windows,text="Click",fg="black",bg="green",command=labelss,font=("Jokerman",10))
name_btn.place(x=800,y=0)
windows.mainloop()
