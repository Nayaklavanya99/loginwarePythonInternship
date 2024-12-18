import sqlite3

con = sqlite3.connect('student.db')

cur = con.cursor()
def userinput():
    global first_name, last_name, email, age
    confirm_name = input("Do you want to add your first_namet? (yes/no): ")
    if confirm_name.lower() == "yes":
        first_name = input("Enter your first name: ")
    else:
        first_name = None
        
        
    confirm_last_name = input("Do you want to add your last_name? (yes/no): ")
    if confirm_last_name.lower() == "yes":
        last_name = input("Enter your last name: ")
    else:
        last_name = None
        
        
    confirm_email = input("Do you want to add your email? (yes/no): ")
    if confirm_email.lower() == "yes":
        email = input("Enter your email: ")
    else:
        email=None
    confirm_age = input("Do you want to add your age? (yes/no): ")
    if confirm_age.lower() == "yes":
        age = input("Enter your age: ")
    else:
        age = None
  
    
userinput()
insert_query = "INSERT INTO students(first_name,last_name,email,age) VALUES(?,?,?,?)"
con.execute(insert_query, (first_name,last_name,email,age))

con.commit()
print("database create")
con.close()
