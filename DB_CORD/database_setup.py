import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="test"
)

mycursor = mydb.cursor()
mycursor.execute("USE food_doctor")

#mycursor.execute('CREATE TABLE customers (test1 INT AUTO_INCREMENT PRIMARY KEY, test2 VARCHAR(255))')

sql = "INSERT INTO customers (test2) VALUES (%s)"
val = ("John",)
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.close()
mydb.close()
