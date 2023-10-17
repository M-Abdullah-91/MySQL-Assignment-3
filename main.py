import mysql.connector as connector

con = connector.connect(host="localhost",
                  user = "root",
                  password = "root",
                  database = "classicmodels")

if con.is_connected():
    print("Successfully connected....")
    
    
cursor = con.cursor()


    

