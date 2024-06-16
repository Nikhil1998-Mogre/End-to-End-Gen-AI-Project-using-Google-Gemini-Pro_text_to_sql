import sqlite3

# connect to sqlite
connection = sqlite3.connect("student.db")

# create a cursor object to insert record,insert table

cursor = connection.cursor()

# create the table
table_info = """
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""

cursor.execute(table_info)

# insert some more records

cursor.execute('''insert into STUDENT values('nikhil',"Data science","A")''')
cursor.execute('''insert into STUDENT values('ketan',"Data science","B")''')
cursor.execute('''insert into STUDENT values('kapil',"Data science","A")''')
cursor.execute('''insert into STUDENT values('raju',"Devops","A")''')
cursor.execute('''insert into STUDENT values('kunal',"Devops","A")''')

# display all the records

print("The inserted records are")
data = cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)


# commit your changes in the database
connection.commit()
connection.close()

