import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM tabulka")
for row in cursor.fetchall():
    print(row)
