

from tkinter import *
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")

name_label1 = None
def closedoperation():
    if name_label1:
        name_label1.destroy()
        #global name_label1
# def open_operation(name):
#     global name_label1 
#     closedoperation()
#     print(name)
#     name_label1=Label(windows,text=name,fg="blue",bg="white",font=("Jokerman",10,"bold","underline"),justify="center")
#     name_label1.place(x=300,y=100,width=300,height=100)

def name_operation():
    global name_label1
    closedoperation()
    name_label1=Label(windows,text="lavanya",fg="blue",bg="white",font=("Jokerman",10,"bold","underline"),justify="center")
    name_label1.place(x=300,y=100,width=300,height=100)
    
def age_operation():
    global name_label1
    closedoperation()
    name_label1=Label(windows,text="22",fg="blue",bg="white",font=("Jokerman",10,"bold","underline"),justify="center")
    name_label1.place(x=300,y=100,width=300,height=100)
def place_operation():
    global name_label1
    closedoperation()
    name_label1=Label(windows,text="Bangalore",fg="blue",bg="white",font=("Jokerman",10,"bold","underline"),justify="center")
    name_label1.place(x=300,y=100,width=300,height=100)
def number_operation():
    global name_label1
    closedoperation()
    name_label1=Label(windows,text="9900443212",fg="blue",bg="white",font=("Jokerman",10,"bold","underline"),justify="center")
    name_label1.place(x=300,y=100,width=300,height=100)
def close_operation():
    global name_label1
    closedoperation()
    if name_label1 == None:
        print("label not found")
        return
    else:
        name_label1.destroy()
    # try:
    #     name_label1.destroy()
    # except:
    #     print("label not found")
    
    

name_label1 = None
    
    
name_btn = Button(windows,text="Name",fg="black",bg="green",command=name_operation,font=("Jokerman",10))
name_btn.place(x=0,y=0)
age_btn = Button(windows,text="Age",fg="black",bg="green",command=age_operation,font=("Jokerman",10))
age_btn.place(x=0,y=40)
place_btn = Button(windows,text="Place",fg="black",bg="green",command=place_operation,font=("Jokerman",10))
place_btn.place(x=0,y=80)
number_btn = Button(windows,text="Number",fg="black",bg="green",command=number_operation,font=("Jokerman",10))
number_btn.place(x=0,y=120)
close_btn = Button(windows,text="Close",fg="black",bg="green",command=close_operation,font=("Jokerman",10))
close_btn.place(x=0,y=160)
windows.mainloop()
