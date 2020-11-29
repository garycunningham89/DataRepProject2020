import mysql.connector

db = mysql.connector.connect{
	host='localhost',
	user="root",
	password="",
	database="datarepresentation"
	)
cursor = db.cursor()
sql = "insert into student(name, address) values (%s, %s)
values = ("Mary", "Galway")
cursor.exectute(sql, values)

db.commit()