def add_employee(conn, employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle):
  cursor = conn.cursor()
  query = "INSERT INTO employees VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"
  values = (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
  cursor.execute(query, values)
  conn.commit()
  print(f"Employee '{firstName,lastName}' added successfully.")
  