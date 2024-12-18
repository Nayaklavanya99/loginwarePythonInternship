
from tkinter import *
window = Tk()
print("window opened")
window.geometry("540x540")
window.title("Calculator")
window.configure(bg="white")

screen = Entry(window, width=30,font=("Arial", 20),bd=4)
screen.place(x=20,y=30)

btn_frame= Frame(window)
btn_frame.place(x=80,y=100)
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]
def clickBtn(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())  
            screen.delete(0, END)
            screen.insert(END, str(result))
        except Exception as e:
            screen.delete(0, END)
            screen.insert(END, "Error")
    elif text == "C":
        screen.delete(0, END)
    else:
        screen.insert(END, text)
row=0
col=0
for button in buttons:
    btn = Button(btn_frame, text=button, font=("Arial", 18), width=5, height=2 , bd=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    
    btn.bind("<Button-1>", clickBtn)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
