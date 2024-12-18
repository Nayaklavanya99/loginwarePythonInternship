
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.messagebox import showinfo
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")
def clickMsg():
    
    msg = messagebox.askquestion("yes", "Are you Mad?")
    
    if msg == "yes":
        messagebox.showinfo("information", "YES YOU ARE RIGHT! ")
    else:
        msg2 = messagebox.showinfo("information", "haha you don't know but u r MAD!!!!!! ")
        if msg2 == "ok":
            msg3 = messagebox.askquestion("yes", "Do you still wanna confirm?")
            if msg3 == "yes":
                messagebox.showerror("error", "YES YOU ARE Strill mad")
            else:
                messagebox.showinfo("information", "you are mad but you are not mad anymore")
            
        #messagebox.showinfo("information", "haha you don't know but u r MAD!!!!!! ")

# messagebox.showinfo( "information", "this is a message box")
# messagebox.showwarning("warning", "this is a warning box")
btn = Button(windows, text="click me", command=clickMsg)
btn.pack()
windows.mainloop()
