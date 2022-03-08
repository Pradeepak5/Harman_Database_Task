import sqlite3 as sql

connection=sql.connect("Company.db")
connection.execute('''create table Employee(
                       Employee_Code integer,
                       Employee_name text,
                       Designation text,
                       Salary integer,
                       company_name text
                       );''')
print("Table is created successfully")

getEmpCode=input("Enter the employee code :")
getempName=input("Enter the employee name :")
getDesignation=input("Enter the designation :")
getSalary=input("Enter your Salary :")
getCompanyName=input("Enter company Name :")

connection.execute("insert into Employee(Employee_Code,Employee_name,Designation,Salary,company_name) \
                    values("+getEmpCode+",'"+getempName+"','"+getDesignation+"',"+getSalary+",'"+getCompanyName+"')")

connection.commit()
connection.close()
print("data is inserted successfully")
