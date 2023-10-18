import pymysql
import query

conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root", 
        db='classicmodels',
        cursorclass=pymysql.cursors.DictCursor
    )

cursor = conn.cursor()

query.add_employee(conn,102, "zain", "Ahmed", "x01","zainahmed@gmail.com", 2, 1002,"President")


