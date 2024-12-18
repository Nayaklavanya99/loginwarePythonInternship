
from tkinter import *
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")
language = ["Kannada","English","Hindi"]
x,y=0,0
choice =StringVar()
lbl = Label(windows, text="Select Language", fg="black", bg="lightgreen", font=("Jokerman", 15))
def on_select():
    select = choice.get()
    print(f"language selected {select}")
for i in language:
    
    radio_btn1 = Radiobutton(windows, text=i, value=i,font=("Arial",15),variable=choice)

    radio_btn1.place(x=x,y=y)
    y+=50
lbl1=None
def on_submit():
    print("Language Submitted: ",choice.get())
    global lbl1
    if lbl1:
        lbl1.destroy()
        lbl1 = None
    lbl1 = Label(windows, text=f"You have Selected: {choice.get()}", fg="black",bg="lightgreen", font=("Jokerman", 15))
    lbl1.place(x=150, y=250)
    
send_btn = Button(windows, text="Send",bg="green",fg="white",font=("bold",15),command=on_submit)
send_btn.place(x=150, y=200)
windows.mainloop()
