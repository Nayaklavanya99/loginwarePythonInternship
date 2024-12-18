from tkinter import *


def file_operations():
    clear_frames()  # Clear existing frames
    file_frame = Frame(window, bg="lightgray", borderwidth=1, relief="solid")
    file_frame.place(x=0, y=30, width=100, height=100)
    Label(file_frame, text="New File", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)
    Label(file_frame, text="Open File", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)
    Label(file_frame, text="Save File", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)
    Label(file_frame, text="Exit", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)


def edit_operations():
    clear_frames()  # Clear existing frames
    edit_frame = Frame(window, bg="lightgray", borderwidth=1, relief="solid")
    edit_frame.place(x=50, y=30, width=100, height=100)
    Label(edit_frame, text="Undo", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)
    Label(edit_frame, text="Redo", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)
    Label(edit_frame, text="Cut", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)
    Label(edit_frame, text="Copy", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)

# Function for View operations
def view_operations():
    clear_frames()  # Clear existing frames
    view_frame = Frame(window, bg="lightgray", borderwidth=1, relief="solid")
    view_frame.place(x=100, y=30, width=100, height=100)
    Label(view_frame, text="Zoom In", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)
    Label(view_frame, text="Zoom Out", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)
    Label(view_frame, text="Full Screen", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)
    Label(view_frame, text="Restore", bg="lightgray", fg="black").pack(fill="x", padx=5, pady=2)

#Function to clear existing frames (close other menus)
def clear_frames():
    for widget in window.winfo_children():
        if isinstance(widget, Frame):
            widget.destroy()

# Create the main window
window = Tk()
window.geometry("860x540")
window.title("Notepad")
window.configure(bg="white")

# Create buttons
File_btn = Button(window, text="File", fg="black", bg="white", font=("Jokerman", 10), justify="center", command=file_operations)
Edit_btn = Button(window, text="Edit", fg="black", bg="white", font=("Jokerman", 10), justify="center", command=edit_operations)
View_btn = Button(window, text="View", fg="black", bg="white", font=("Jokerman", 10), justify="center", command=view_operations)

# Place buttons
File_btn.place(x=0, y=0)
Edit_btn.place(x=50, y=0)
View_btn.place(x=100, y=0)

window.mainloop()
