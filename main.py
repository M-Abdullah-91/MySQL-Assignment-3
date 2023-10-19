import pymysql
import query
import json


    
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
            Press 11 to exit \n""")
    
user_input = int(input("Enter a Number: "))
    
if user_input == 1:
    query.add_employee(conn)
    
elif user_input == 2:
    query.add_customer(conn)
    
elif user_input == 3:
    query.add_order(conn)
    
elif user_input == 4:
    query.add_payment_details(conn)
    
elif user_input == 5:
    query.show_stats(conn)
    
elif user_input == 6:
    employees = query.show_employees(conn)
    print(json.dumps(employees, default=str, indent=4))
    
elif user_input == 7:
    employees_city_and_country = query.employees_city_and_country(conn)
    print(json.dumps(employees_city_and_country, default=str, indent=4))
    
elif user_input == 8:
    product_name = query.product_name(conn)
    print(json.dumps(product_name, default=str, indent=4))
    
elif user_input == 9:
    captures_customer = query.captures_customer(conn)
    print(json.dumps(captures_customer, default=str, indent=4))
    
elif user_input == 10:
    did_not_capture_customer = query.did_not_captures_customer(conn)
    print(json.dumps(did_not_capture_customer, default=str, indent=4))  
else :
    print("Thank you..")


# add 10 employees
def add_10_employee(conn):
    for i in range(1,11):
        query.add_employee(conn)
        
        