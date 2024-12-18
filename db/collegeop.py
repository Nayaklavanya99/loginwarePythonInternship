import sqlite3

conn = sqlite3.connect("College.db")
cur = conn.cursor()


conn.commit()
conn.close()
