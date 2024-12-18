

from tkinter import *
from tkinter.ttk import Progressbar
from time import sleep
from tkinter import messagebox
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")

def move():
    # for i in range(0,101,10):
    #     progressbar['value'] = i
    #     windows.update_idletasks()
    #     progressbar3['value'] = i
    #     windows.update_idletasks()
    #     progressbar4['value'] = i
    #     windows.update_idletasks()
    #     progressbar5['value'] = i
    #     windows.update_idletasks()
    #     progressbar2['value'] = i
    #     windows.update_idletasks()
    #     sleep(0.1)
    # for i in range(101,0,-10):
    #     progressbar['value'] = i
    #     windows.update_idletasks()
    #     progressbar3['value'] = i
    #     windows.update_idletasks()
    #     progressbar4['value'] = i
    #     windows.update_idletasks()
    #     progressbar5['value'] = i
    #     windows.update_idletasks()
    #     progressbar2['value'] = i
    #     windows.update_idletasks()
    #     sleep(0.1)
    # move()
    progressbar2.start(1)
    progressbar3.start(2)
    progressbar4.start(3)
    progressbar5.start(4)
    
    progressbar.start(10)
def end():
    msg = messagebox.askquestion("exit", "do you want to exit")
    if msg == "yes":
        
        progressbar.stop()
        progressbar3.stop()
        progressbar4.stop()
        progressbar5.stop()
    else:
        move()
        
    
    progressbar2.stop() 
progressbar = Progressbar(windows, orient=HORIZONTAL, length=400, mode='determinate', phase=20, value=50)
progressbar.pack(pady=10)
progressbar2 = Progressbar(windows, orient=HORIZONTAL, length=400, mode='indeterminate', value=10)
progressbar2.pack(pady=30)
progressbar3 = Progressbar(windows, orient=HORIZONTAL, length=400, mode='determinate', phase=20, value=50)
progressbar3.pack(pady=50)



progressbar4 = Progressbar(windows, orient=VERTICAL, length=400, mode='determinate', phase=20, value=50)
progressbar4.place(x=30,y=0)
progressbar5 = Progressbar(windows, orient=VERTICAL, length=400, mode='determinate', phase=20, value=50)
progressbar5.place(x=800,y=0)


btn = Button(windows, text="move", command=move)
btn.pack(pady=10)
btn2 = Button(windows, text="stop", command=end)
btn2.pack(pady=20)
windows.mainloop()
