import sqlite3

conn = sqlite3.connect("tasksdb.db")
cur = conn.cursor()

# cur.execute("INSERT INTO Person(name, age) VALUES('eve',21)")
# cur.execute("INSERT INTO Person(name, age) VALUES('eve', 99)")
select_query1 = """SELECT name,COUNT(NAME) FROM Person  GROUP BY name ORDER BY name DESC"""
cur.execute(select_query1)

select_query2 = """SELECT name, SUM(age) FROM Person GROUP BY name """
cur.execute(select_query2)

select_query3 = """SELECT name, max(age) AS age FROM Person WHERE age = age """
cur.execute(select_query3)
print(cur.fetchall())
select_query4 = """SELECT name, min(age) AS age FROM Person WHERE age = age """
cur.execute(select_query4)
print(cur.fetchall())
select_query5 = """SELECT name, avg(age) AS age FROM Person WHERE age = age """
cur.execute(select_query5)
print(cur.fetchall())
conn.commit()
conn.close()
