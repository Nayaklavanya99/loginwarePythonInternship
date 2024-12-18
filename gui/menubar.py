
from tkinter import *
from tkinter.ttk import Menubutton
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")


menubar = Menu(windows)
File = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=File)
file_operation=["New","Open","","Save","Save As","","Rename","Delete","Exit"]
for i in file_operation:
    if i == "":
        File.add_separator()
        continue
    elif i == "Exit":
        File.add_command(label=i,command=windows.destroy)
    
    File.add_command(label=i)
    
Edit = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit", menu=Edit)
edit_operation=["Cut","Copy","Undo","Redo"]
for i in edit_operation:
    Edit.add_command(label=i)

View = Menu(menubar,tearoff=0)
menubar.add_cascade(label="View", menu=View)
view_operation=["Zoom-in","Zoom-out","Full-Screen","Restore"]
for i in view_operation:
    View.add_command(label=i)
Menu.configure(windows,menu=menubar)
windows.mainloop()
