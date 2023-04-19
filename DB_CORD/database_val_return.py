import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="test",
  database="testdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT test2 FROM customers WHERE test1 = 2")

result = mycursor.fetchone()

print(result[0])