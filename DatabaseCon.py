import mysql.connector

cnx = mysql.connector.connect(user='master', password='master', host='localhost', database='master')
cursor = cnx.cursor()

query = ("INSERT INTO successor (event, followingEvents) VALUES ('B', '4')")

cursor.execute(query)
cnx.commit()