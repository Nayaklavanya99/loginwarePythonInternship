
from tkinter import *
from tkinter import IntVar
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")
choice = IntVar()
lbl2 = None
def clicked(value):
    
    global lbl2
    if lbl2:
        lbl2.destroy()
    # print(choice.get())
    lbl2 = Label(windows, text=f"You have choosed: {value}", fg="blue", font=("Jokerman", 15))
    lbl2.place(x=230, y=290)
    try:
        windows.configure(bg=f"#ff{str(value)}{str(value)}")
        
        lbl2.configure(bg="red",fg="white")
    except:
        windows.configure(bg=f"#ff{str(value)}")
        
        lbl2.configure(bg="red",fg="white")
    # if (int(value) %2 )== 0:
    #     scale.configure(bg="pink", fg="black")
    #     windows.configure(bg="green")
    #     lbl2.configure(bg="red",fg="white")
    # else:
    #     scale.configure(bg="black", fg="pink")
    #     windows.configure(bg="blue")
    #     lbl2.configure(bg="yellow",fg="black")

scale = Scale(windows,cursor="circle",command=clicked,variable=choice,showvalue=False ,from_=0,to=100,orient=VERTICAL,bg="lightblue",fg="black",font=(10),width=20,length=200,activebackground="green",troughcolor="lightgreen",tickinterval=10)

# btn = Button(windows, text="Send", command=clicked,bg="green",fg="white",font=("bold",15))
# btn.place(x=230, y=390)
scale.place(x=10,y=10)
windows.mainloop()
