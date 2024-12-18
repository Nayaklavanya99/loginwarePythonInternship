

from tkinter import *
from tkinter.ttk import *
from tkinter import Toplevel
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")

def createWindow():
    windows1 = Toplevel()
    windows1.geometry("160x140")
    windows1.title("notepad")
    windows1.configure(bg="black")
    windows1.mainloop()

btn = Button(windows,text="click",command=createWindow)
btn.pack()
windows.mainloop()
