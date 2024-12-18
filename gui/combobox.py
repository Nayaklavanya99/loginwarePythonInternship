
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Checkbutton
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")

def check():
    options.append(combobox.get())
    print(options)
    label = Label(windows, text=combobox.get(), bg="lightblue",font=("Jokerman",10,"bold","underline"),justify="center")
    label.pack()
lang = ["Kannada","English","Hindi"]
list = ["Date","Month","Year"]
datelist=["22","12","24"]
monthlist=["July","September","April"]
yearlist=["2002","2002","1998"]
options=[]
x=0
y=0
k=0
for i in [datelist,monthlist,yearlist]:
    
    combobox = Combobox(windows,font=("Jokerman",10,"bold","underline"),justify="center",state="readonly",width=10)
    combobox["values"] = i[0:]
    print(f"selected: {combobox['values']}")
    combobox.set(list[k])
    options.append(combobox.get())
    k+=1
    combobox.place(x=x,y=y)
    x+=250
    

send_btn = Button(windows, text="Send",command=check)
send_btn.place(x=250,y=50)
windows.mainloop()
