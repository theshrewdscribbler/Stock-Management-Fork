import sqlite3
conn=sqlite3.connect("management.db")
cursor=conn.cursor()
conn.close()