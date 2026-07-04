import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# -----------------------
# Departments
# -----------------------

departments = [

(1,'IT'),
(2,'HR'),
(3,'Finance'),
(4,'Sales')

]

cursor.executemany(
"INSERT INTO Departments VALUES (?,?)",
departments)

# -----------------------
# Employees
# -----------------------

employees = [

(101,'Alice',1,85000,'2021-01-15',None),

(102,'Bob',1,75000,'2021-03-12',101),

(103,'Charlie',1,75000,'2022-06-20',101),

(104,'David',2,60000,'2020-02-18',None),

(105,'Eva',2,55000,'2023-05-10',104),

(106,'Frank',3,90000,'2019-07-25',None),

(107,'Grace',3,82000,'2020-11-30',106),

(108,'Henry',4,65000,'2021-09-12',None),

(109,'Ivy',4,65000,'2022-04-15',108),

(110,'Jack',4,50000,'2023-08-20',108),

(111,'Kevin',1,95000,'2018-10-01',None),

(112,'Linda',3,90000,'2019-01-17',106)

]

cursor.executemany(
"INSERT INTO Employees VALUES (?,?,?,?,?,?)",
employees)

# -----------------------
# Projects
# -----------------------

projects=[

(1,'Customer Portal',500000),

(2,'HR Automation',300000),

(3,'Finance Dashboard',450000),

(4,'Sales Analytics',600000),

(5,'AI Chatbot',800000)

]

cursor.executemany(
"INSERT INTO Projects VALUES (?,?,?)",
projects)

# -----------------------
# Employee Project Mapping
# -----------------------

mapping=[

(101,1),
(101,5),

(102,1),

(103,5),

(104,2),

(105,2),

(106,3),

(107,3),

(108,4),

(109,4),

(111,5)

]

cursor.executemany(
"INSERT INTO Employee_Project VALUES (?,?)",
mapping)

conn.commit()

print("Data Inserted Successfully")

conn.close()

