import sqlite3

conn = sqlite3.connect("../temperature_db")

cursor = conn.cursor()

conn.commit()
conn.close()
