import sqlite3

conn = sqlite3.connect("library.db")

cur = conn.cursor()
cur.execute("drop table books")
create_query = '''CREATE TABLE IF NOT EXISTS books (
    Book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    Price REAL 
)'''
cur.execute(create_query)

insert_query = """INSERT INTO books(Title,Author,Price) VALUES('c-programming','george orwell',1001),
('Metamorphosis','Franz Kafka',200),
('Metamorpho','Franz Kafka',5000),
('Cprogramming','george orwell',8.99)"""
cur.execute(insert_query)



select_query4 = """SELECT DISTINCT(Author) FROM books WHERE Price <1000 or Price >20"""
cur.execute(select_query4)
print(cur.fetchall()[0][0])

conn.commit()
print("database create")
conn.close()
