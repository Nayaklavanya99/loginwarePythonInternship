from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import Toplevel
def validate_and_save():
    
    if choice.get() == "":
        messagebox.showerror("Error", "Please select a gender")
        return False
        
    if list1[0].get() == "":
        messagebox.showerror("Error", "Please enter your name")
        return False

    if list1[1].get() == "":
        messagebox.showerror("Error", "Please enter your age")
        return False
    elif not list1[1].get().isnumeric():
        messagebox.showerror("Error", "Age must be a number")
        return False
    elif not (1 <= int(list1[1].get()) <= 120):
        messagebox.showerror("Error", "Please enter a valid age between 1 and 120")
        return False
    
  
    if list1[2].get() == "":
        messagebox.showerror("Error", "Please enter your phone number")
        return False
    elif not list1[2].get().isnumeric():
        messagebox.showerror("Error", "Phone number must contain only digits")
        return False
    elif len(list1[2].get()) != 10:
        messagebox.showerror("Error", "Phone number must be 10 digits")
        return False
            
    # Validate email
    if list1[3].get() == "":
        messagebox.showerror("Error", "Please enter your email")
        return False
    elif "@" not in list1[3].get() or not list1[3].get().endswith(".com"):
        messagebox.showerror("Error", "Please enter a valid email address")
        return False
            
    # Validate college name
    if list1[4].get() == "":
        messagebox.showerror("Error", "Please enter your college name")
        return False
        
    # Validate course
    if list1[5].get() == "":
        messagebox.showerror("Error", "Please enter your course")
        return False

    # If all validations pass, save the data
    save_data()
    return True

def save_data():
    name = list1[0].get()
    age = list1[1].get()
    phone = list1[2].get()
    email = list1[3].get()
    college = list1[4].get()
    course = list1[5].get()
    usn = list1[6].get()
    gender = choice.get()
    
    con = sqlite3.connect('register.db')
    cur = con.cursor()
    
    create_query = """CREATE TABLE IF NOT EXISTS `users` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `name` TEXT NOT NULL,
        `age` INTEGER NOT NULL,
        `phone` TEXT NOT NULL,
        `email` TEXT NOT NULL,
        `college` TEXT NOT NULL,
        `course` TEXT NOT NULL,
        `usn` TEXT NOT NULL DEFAULT NULL,
        `gender` TEXT NOT NULL
        )"""
    cur.execute(create_query)
    # insert_query = "INSERT INTO users(name, age, phone, email, college, course, usn, gender) VALUES(?,?,?,?,?,?,?,?)"
    # cur.execute(insert_query, (name, age, phone, email, college, course, usn, gender))
    
    
    
    
    con.commit()
    print("database create")
    con.close()
    window.destroy()
    window2 = Tk()
    window2.title("Completed!")
    window2.geometry("500x200")
    window2.configure(bg="#f0f0f0")
    success_label = Label(window2,
                         text="Thank You 😊\n\nYou Have Sucessfully Registered 👍!",
                         font=("Arial", 20),
                         bg="#f0f0f0",
                         fg="blue",
                         pady=20,padx=20)
    success_label.pack()
    window2.mainloop()
    

    

def send():
    validate_and_save()
    
# Window setup
window = Tk()
window.title("Student Registration Form")
window.geometry("600x700")
window.configure(bg="#f0f0f0")

# Main heading
heading = Label(window, 
               text="Student Registration Form",
               font=("Arial", 20, "bold"),
               bg="#f0f0f0",
               fg="#333333",
               pady=20)
heading.pack()

# Create main frame
main_frame = Frame(window, bg="#f0f0f0")
main_frame.pack(padx=40, pady=20)

# Variables
list1 = []
list2 = ["Full Name", "Age", "Phone Number", "Email ID", "College", "Course", "USN", "Gender"]

# Create form fields
for i in range(len(list2)-1):
    field_frame = Frame(main_frame, bg="#f0f0f0")
    field_frame.pack(pady=10)
    
    label = Label(field_frame, 
                 text=list2[i],
                 font=("Arial", 12),
                 bg="#f0f0f0",
                 width=15,
                 anchor="w")
    label.pack(side=LEFT)
    
    entry = Entry(field_frame,
                 font=("Arial", 12),
                 width=30)
    entry.pack(side=LEFT, padx=10)
    list1.append(entry)

# Gender selection
gender_frame = Frame(main_frame, bg="#f0f0f0")
gender_frame.pack(pady=10)

gender_label = Label(gender_frame,
                    text="Gender",
                    font=("Arial", 12),
                    bg="#f0f0f0",
                    width=15,
                    anchor="w")
gender_label.pack(side=LEFT)

choice = StringVar()
genders = ["Male", "Female", "Others"]

radio_frame = Frame(gender_frame, bg="#f0f0f0")
radio_frame.pack(side=LEFT)

for gender in genders:
    radio_btn = Radiobutton(radio_frame,
                           text=gender,
                           value=gender,
                           variable=choice,
                           font=("Arial", 11),
                           bg="#f0f0f0")
    radio_btn.pack(side=LEFT, padx=10)

# Submit button
button_frame = Frame(main_frame, bg="#f0f0f0")
button_frame.pack(pady=20)

submit_btn = Button(button_frame,
                   text="Submit",
                   command=send,
                   font=("Arial", 12, "bold"),
                   bg="#4CAF50",
                   fg="white",
                   padx=20,
                   pady=10,
                   cursor="hand2")
submit_btn.pack()

window.mainloop()
