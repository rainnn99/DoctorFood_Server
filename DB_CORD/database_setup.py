# import mysql.connector

# mydb = mysql.connector.connect(
#    host="localhost",
#    user="test",
#    password="test"
# )

# mycursor = mydb.cursor()
# mycursor.execute("USE testdb")

# mycursor.execute('CREATE TABLE customers (test1 INT AUTO_INCREMENT PRIMARY KEY, test2 VARCHAR(255))')

# sql = "INSERT INTO customers (test2) VALUES (%s)"
# val = ("John",)
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)

# mycursor.close()
# mydb.close()


# ------------------------------------------------------------------------
# pip install pymysql
import csv
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""  # 비밀번호
)

mycursor = mydb.cursor()
mycursor.execute("create database food_doctor;")  # 데이터베이스 만들기
mycursor.execute("USE food_doctor")

# 음식 테이블
# ------------------------------------------------------
mycursor.execute("create table food(\
food_small_scale_classification VARCHAR(12) NOT NULL,\
food_no INT,\
food_large_scale_classification VARCHAR(9),\
food_medium_scale_classification VARCHAR(9),\
serving_size_g INT,\
calorie_g FLOAT,\
protein_g FLOAT,\
fat_g FLOAT,\
carbohydrate_g FLOAT,\
salt_mg FLOAT,\
PRIMARY KEY(food_small_scale_classification)\
);")
# ------------------------------------------------------


# 고객 테이블(프론트에서 입력받는 항목 보고 수정 필요)
# ------------------------------------------------------
# mycursor.execute("CREATE TABLE customer(\
# id VARCHAR(12) NOT NULL,\
# password VARCHAR(20),\
# name VARCHAR(4),\
# birth DATE,\
# sex CHAR(1),\
# phone_number VARCHAR(11),\
# email VARCHAR(30),\
# job VARCHAR(15),\
# height FLOAT,\
# weight FLOAT,\
# bmi FLOAT,\
# CONSTRAINT customer_PK PRIMARY KEY(id)\
# );")
# ------------------------------------------------------

# 질병 테이블
# ------------------------------------------------------
# mycursor.execute("CREATE TABLE disease(\
# customer_id VARCHAR(12),\
# disease VARCHAR(6),\
# CONSTRAINT disease_PK PRIMARY KEY(customer_id, disease),\
# CONSTRAINT disease_FK FOREIGN KEY (customer_id) references customer(id)\
# );")
# ------------------------------------------------------

# 선호음식 테이블
# ------------------------------------------------------
# mycursor.execute("CREATE TABLE preferred_food(\
# customer_id VARCHAR(12),\
# food_small_scale_classification VARCHAR(12),\
# CONSTRAINT preferred_food_PK PRIMARY KEY(customer_id, food_small_scale_classification),\
# CONSTRAINT preferred_food_FK FOREIGN KEY (customer_id) references customer(id),\
# CONSTRAINT preferred_food_FK2 FOREIGN KEY (food_small_scale_classification) references food(food_small_scale_classification)\
# );")
# ------------------------------------------------------

# 건강식 테이블
# ------------------------------------------------------
# mycursor.execute("CREATE TABLE healthy_food(\
# customer_id VARCHAR(12),\
# food_small_scale_classification VARCHAR(12),\
# CONSTRAINT healthy_food_PK PRIMARY KEY(customer_id, food_small_scale_classification),\
# CONSTRAINT healthy_food_FK FOREIGN KEY (customer_id) references customer(id),\
# CONSTRAINT healthy_food_FK2 FOREIGN KEY (food_small_scale_classification) references food(food_small_scale_classification)\
# );")
# ------------------------------------------------------

# food.csv파일 mysql에 삽입
# ------------------------------------------------------

with open('food.csv', "r", encoding='UTF8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sql = "INSERT INTO food (food_no, food_large_scale_classification, food_medium_scale_classification, food_small_scale_classification, serving_size_g,\
            calorie_g, protein_g, fat_g, carbohydrate_g, salt_mg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (row['food_no'], row['food_large_scale_classification'], row['food_medium_scale_classification'], row['food_small_scale_classification'], row['serving_size_g'],
               row['calorie_g'], row['protein_g'], row['fat_g'], row['carbohydrate_g'], row['salt_mg'])
        mycursor.execute(sql, val)
# ------------------------------------------------------

mydb.commit()
mycursor.close()
mydb.close()
