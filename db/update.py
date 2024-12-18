import sqlite3

conn = sqlite3.connect("library.db")

cur = conn.cursor()
val = ["Pearson"]
update_query = """UPDATE books SET Publisher=? where price >1000"""
cur.execute(update_query,val)

select_query1 = """SELECT * FROM books"""
cur.execute(select_query1)
for i in cur.fetchall():
    print(i)

conn.commit()

conn.close()