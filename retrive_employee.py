import sqlite3 as sql

connection=sql.connect("Company.db")

result=connection.execute("select * from Employee")

for i in result:
    print(i)