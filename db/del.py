import sqlite3

conn = sqlite3.connect("library.db")

cur = conn.cursor()
delete_query = """DELETE FROM books WHERE Book_id in (SELECT Book_id FROM books order by Book_id desc limit 1)"""
cur.execute(delete_query)


select_query1 = """SELECT * FROM books"""
cur.execute(select_query1)
for i in cur.fetchall():
    print(i)

conn.commit()
conn.close()