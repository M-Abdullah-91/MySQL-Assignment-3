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

print("""
            press 1 to add employee
            press 2 to add customers
            press 3 to add orders
            press 4 to add payment detail
            press 5 to show dashboard stats
            press 6 to show all employees
            press 7 to show all employees (name) along with the city and country name they are working and their job title
            press 8 to show all product name and price and product category name
            press 9 to show all employees name who captures the customer
            press 10 to show all employees who didn't suceed in capturing the customer
            press 11 to show the employee names along with the sale they managed to capture by customer""")
    
user_input = int(input("Enter a Number: "))
    
if user_input == 1:
    query.add_employee(conn)
elif user_input == 2:
    query.add_customer(conn)
elif user_input == 3:
    pass
elif user_input == 4:
    pass
elif user_input == 5:
    query.show_stats(conn)
elif user_input == 6:
    pass
elif user_input == 7:
    pass
elif user_input == 8:
    pass
elif user_input == 9:
    pass
elif user_input == 10:
    pass
elif user_input == 11:
    pass
else :
    print("End..")
# query.add_employee(conn,102, "zain", "Ahmed", "x01","zainahmed@gmail.com", 2, 1002,"President")


