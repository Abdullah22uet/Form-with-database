# start of code
# form with database
import time
import mysql.connector as c
data = c.connect(host="localhost",port="3306",user="root",password="admin123#",database="formdata")
curser = data.cursor()
query = "CREATE TABLE IF NOT EXISTS userData (name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))"
curser.execute(query)
print("\n\t\t *************** FORM ***************")
print("Enter your details :----")
name = input("Enter your name : ")
email = input("Enter your email : ")
password = input("Enter your password : ")
query2 = "INSERT INTO userData (name, email, password) VALUES ('{name}','{email}','{password}')".format(name=name,email=email,password=password)
print("\nLoading",end="")
for i in range(3):
    print(".",end="",flush=True)
    time.sleep(0.7)
print("\nYour data is saved successfully...")
curser.execute(query2)
data.commit()
data.close()
# end of code