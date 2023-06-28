import mysql.connector

conn = mysql.connector.connect(username='root', password='12345',database='fr')
cursor = conn.cursor()

cursor.execute("show tables")

data = cursor.fetchall()

print(data)

conn.close()