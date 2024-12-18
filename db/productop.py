import sqlite3
conn = sqlite3.connect("productsdb.db")
cur = conn.cursor()




# try:
#     cur.execute("""INSERT INTO Product(name, price) VALUES("ball",2)""")
# except sqlite3.IntegrityError as e:
#     print("Please enter valid input\n",e)
# except Exception as e:
#     print(f"Failed: {e}")
# else:
    # select_query1 = """SELECT COUNT(prouct_id) FROM Product"""
    # cur.execute(select_query1)
    # list_product = cur.fetchall()
    # for i in list_product:
    #     print(i)

# try:
#     cur.execute("Drop TABLE Product")
# except sqlite3.DatabaseError as e:
#     print(e)
# except Exception as e:
#     print("Failed to drop",e)
    
select = """SELECT COUNT(product_id) FROM Product"""
cur.execute(select)
print(cur.fetchall()[0][0])
    






conn.commit()
conn.close()