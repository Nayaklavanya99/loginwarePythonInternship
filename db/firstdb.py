import sqlite3

con = sqlite3.connect('student.db')

cur = con.cursor()


create_query = '''CREATE TABLE IF NOT EXISTS students (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL ,
    age INTEGER NOT NULL
)'''

cur.execute(create_query)
delete_query = "DELETE FROM students WHERE age BETWEEN 22 AND 25"
# cur.execute(delete_query)
insert_query = "INSERT INTO students(first_name,last_name,email,age) VALUES(?,?,?,?)"
# insert_query = """INSERT INTO students VALUES('John','Doe','john.doe@example.com',25),
# ('sahil','belurkar','sahilbelur@example.com',22),
# ('lavanya','nayak','lavanayak@example.com',23)"""

cur.execute(insert_query,('lavi','','',22))


# describe = """PRAGMA TABLE_INFO("students")"""
# cur.execute(describe)

# SELECT_QUERY = "SELECT * FROM students WHERE first_name='sahil'"
# cur.execute(SELECT_QUERY)
# # Print all rows from the query result
# for row in cur.fetchall():
#     print(f"First Name: {row[0]}")
#     print(f"Last Name: {row[1]}")
#     print(f"Email: {row[2]}")
#     print(f"Age: {row[3]}")
#     print("-" * 20)#fetch select


con.commit()
print("database create")
con.close()