import sqlite3

conn = sqlite3.connect("library.db")

cur = conn.cursor()

# select_query1 = """SELECT * FROM books WHERE Book_id not in (2,3)"""
# cur.execute(select_query1)

# select_query2 = """SELECT * FROM books WHERE Price > 1000"""
# cur.execute(select_query2)

# books = cur.fetchall()
# for row in books:
#     print(f"Book ID: {row[0]}")
#     print(f"Title: {row[1]}")
#     print(f"Author: {row[2]}")
#     print(f"Price: {row[3]}")
#     print("-----------------------------------------------------------")
# select_query3 = """SELECT DISTINCT(Author) FROM books WHERE Price <1000 and Price >20"""
# cur.execute(select_query3)

# select_query4 = """SELECT DISTINCT(Author) FROM books WHERE Price <1000 or Price >20"""
# cur.execute(select_query4)
# print(cur.fetchall()[0][0])

alter_query = """ALTER TABLE books ADD COLUMN Publisher TEXT"""
cur.execute(alter_query)

# select_query5 = """SELECT * FROM books ORDER BY Price ASC"""
# cur.execute(select_query5)

# select_query6 = """SELECT Title FROM books ORDER BY Price DESC  LIMIT 1"""
# cur.execute(select_query6)

select_query7 = """SELECT * FROM books WHERE Book_id BETWEEN 1 AND 4 ORDER BY Title ASC"""
cur.execute(select_query7)
for i in cur.fetchall():
    print(i)




conn.commit()
print("database create")
conn.close()