import sqlite3
conn = sqlite3.connect("productsdb.db")
cur = conn.cursor()



try:
    create_product = """CREATE TABLE IF NOT EXISTS Product (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL ,
        price REAL CHECK (price > 0),
        quantity INTEGER NOT NULL DEFAULT 0)"""
except sqlite3.Error as e:
    print("Failed to create product: ",e)
except Exception as e:
    print("Failed to create product: ",e)

else:
    cur.execute("Drop TABLE IF EXISTS Product")

cur.execute(create_product)
details = [
    (1,"TV",25000,1),
    (2,"macbook",400000,1),
    (3,"pencil",5,20),
    (4,"bottle",390,2),
    (5,"charger",990,3)
]

insert_product = """INSERT INTO Product (product_id, name, price,quantity) VALUES(?,?,?,?)"""
cur.executemany(insert_product, details)



conn.commit()
conn.close()
