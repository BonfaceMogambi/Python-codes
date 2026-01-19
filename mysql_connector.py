import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gambigeeks@96",
  database="mydatabase"

)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students (name VARCHAR(255), age VARCHAR(255))")
print (f"The table created successfully")

