from datetime import date

def add_employee(conn):
    employeeNumber = input("Enter employeeNumber: ") 
    lastName = input("Enter last name: ")
    firstName = input("Enter first name: ")
    extension = input("Enter extension: ") 
    email= input("Enter email:  ") 
    officeCode = input("Enter office code: ") 
    reportsTo = input("Enter reportsTo: ") 
    jobTitle = input("Enter job title: ")
    query = "INSERT INTO employees VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"
    cursor = conn.cursor()
    values = (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
    cursor.execute(query, values)
    conn.commit()
    print(f"Employee '{firstName+lastName}' added successfully.")
  
def add_customer(conn):
  customerNumber = input("Enter Customer ID: ")
  customerName = input("Enter your name: ")
  contactLastName = input("Enter contactLastName: ")
  contactFirstName = input("Enter contactFirstName: ")
  phone = input("Enter phoneNumber: ")
  addressLine1 = input("EnteraddressLine: ")
  addressLine2 = input("Enter addressLine2: ")
  city = input("Enter city: ")
  state = input("Enter state: ")
  postalCode = input("Enter postalcode: ")
  country = input("Enter country: ")
  salesRepEmployeeNumber = input("Enter SalesRepEmployeeNumber: ")
  creditLimit = input("Enter creditLimit: ")
  cursor = conn.cursor()
  query = "INSERT INTO customers VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
  values = (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
  cursor.execute(query, values)
  conn.commit()
  print(f"Customer '{customerName}' added successfully.")
  
def add_order(conn):
  orderNumber  = input("Enter order number: ")
  orderDate  = input("Enter order date: ")
  requiredDate = input("Enter required date: ")
  shippedDate  = input("Enter shipping date: ")
  status = input("Enter status(shipped/cancelled)")
  comments = input("Enter comments")
  customerNumber = input("Enter customer number")
  cursor = conn.cursor()
  query = "INSERT INTO employees VALUES (%s, %s, %s, %s,%s, %s, %s)"
  values = (orderNumber, orderDate, date(requiredDate), date(shippedDate), status, comments, customerNumber)
  cursor.execute(query, values)
  conn.commit()
  print("Added successfully.")
  
def add_payment_details(conn, customernumber, checknumber, paymentdate, amount):
  cursor = conn.cursor()
  query = "INSERT INTO employees VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"
  values = (customernumber, checknumber, date(paymentdate), amount)
  cursor.execute(query, values)
  conn.commit()
  print("Added successfully.")
  
  
def show_stats(conn):
  cursor = conn.cursor()
  total_employees = cursor.execute("SELECT * FROM employees")
  total_customers = cursor.execute("SELECT * FROM customers")
  total_payment = cursor.execute("SELECT * FROM payments")
  total_order = cursor.execute("SELECT * FROM orders")
  total_product = cursor.execute("SELECT * FROM products;")
  conn.commit()
  print("Total Employees: ",total_employees)
  print("Total Customer: ",total_customers)
  print("Total payments: ",total_payment)
  print("Total Order: ",total_order)
  print("Total Products: ",total_product)
  
  
def show_employees(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM employees")
  
  
  

  