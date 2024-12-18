import sqlite3
conn = sqlite3.connect("tasksdb.db")
cur = conn.cursor()
cur.execute("Drop TABLE IF EXISTS Person")
try:
    create_task = """CREATE TABLE IF NOT EXISTS Person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
        )"""
    cur.execute(create_task)
except sqlite3.DataError as e:
    print("Failed to create task: ",e)
    
try:
    data = [
        ("Alice", 30),
        ("Bob", 25), 
        ("Charlie", 35),
        ("David", 28),
        ("Eve", 22)
    ]
    insert_task = """INSERT INTO Person (name, age) VALUES (?,?)"""
    cur.executemany(insert_task, data)
except sqlite3.IntegrityError as e:
    print("Failed to insert task: ", e)
    
select_task = """SELECT * FROM Person"""
cur.execute(select_task)
for i in cur.fetchall():
    print(i)
conn.commit()
conn.close()
