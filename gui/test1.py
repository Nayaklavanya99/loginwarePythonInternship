

from tkinter import *
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")


def name_operation(name):
    name_label1=Label(windows,text=name,fg="blue",bg="white",font=("Jokerman",10,"bold","underline"),justify="center")
    return name_label1.place(x=300,y=100,width=300,height=100)
def age_operation(age):
    name_label1=Label(windows,text=age,fg="blue",bg="white",font=("Jokerman",10,"bold","underline"),justify="center")
    return name_label1.place(x=300,y=100,width=300,height=100)
def close_operation():
    global name_label1
    #closedoperation()
    if name_label1 == None:
        print("label not found")
        return
    else:
        name_label1.destroy()

name_label1 = None 

name_btn = Button(windows,text="Name",fg="black",bg="green",command=name_operation("lavanya"),font=("Jokerman",10))
name_btn.place(x=0,y=0)
age_btn = Button(windows,text="Age",fg="black",bg="green",command=age_operation(22),font=("Jokerman",10))
age_btn.place(x=0,y=40)

close_btn = Button(windows,text="Close",fg="black",bg="green",command=close_operation,font=("Jokerman",10))
close_btn.place(x=80,y=0)
windows.mainloop()
