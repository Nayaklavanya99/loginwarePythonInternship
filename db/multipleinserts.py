import sqlite3

con = sqlite3.connect('student.db')

cur = con.cursor()

details = [
    ("ram","nayak","ram@gmail.com",21),
    ("shyam", "nayak", "shyam@gmail.com", 22),
    ("lavi", "nayak", "XXXXXXXXXXXXXX", 23),
    ("sahil", "belurkar", "XXXXXXXXXXXXXXX", 24),
    ("lavanayak", "nayak", "XXXXXXXXXXXXXXXXXXX", 25),
    ("lavanayak", "nayak", "XXXXXXXXXXXXXXXXXXX", 25),
    ("lavanayak", "nayak", "XXXXXXXXXXXXXXXXXXX", 25),  
]
insert_query = "INSERT INTO students(first_name,last_name,email,age) VALUES(?,?,?,?)"
cur.executemany(insert_query, details)


con.commit()
print("using students db")
con.close()
