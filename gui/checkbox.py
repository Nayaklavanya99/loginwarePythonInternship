
from tkinter import *
from tkinter import Checkbutton
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")
language = ["Kannada","English","Hindi"]
x,y=0,0
choice = StringVar()
def click():
    print(f"clicked : {choice.get()}")
# for i in language:
#     check = Checkbutton(windows,text=i,fg="blue",bg="white",font=("Jokerman",10,"bold","underline"),justify="center",onvalue=i,offvalue=None,variable=choice)
#     check.place(x=x,y=y)
#     y+=50
# send_btn = Button(windows, text="Send",bg="green",fg="white",font=("bold",15),command=check)
# send_btn.place(x=150, y=200)
check = Checkbutton(windows,text="kannada",fg="blue",bg="white",font=("Jokerman",10,"bold","underline"),justify="center",onvalue=1,offvalue=None,variable=choice,command=click)
check.pack()

windows.mainloop()
