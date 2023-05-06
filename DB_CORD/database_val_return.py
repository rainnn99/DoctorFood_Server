# import mysql.connector

# mydb = mysql.connector.connect(
#    host="localhost",
#    user="test",
#    password="test",
#    database="testdb"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT test2 FROM customers WHERE test1 = 2")

# result = mycursor.fetchone()

# print(result[0])


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # 비밀번호 입력
    database="food_doctor"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT test2 FROM customers WHERE test1 = 2")

result = mycursor.fetchone()

print(result[0])
