import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Drop tables if they already exist
cursor.executescript("""

DROP TABLE IF EXISTS Employee_Project;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;

""")

# ----------------------------
# Departments
# ----------------------------

cursor.execute("""

CREATE TABLE Departments(
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT
)

""")

# ----------------------------
# Employees
# ----------------------------

cursor.execute("""

CREATE TABLE Employees(
    EmployeeID INTEGER PRIMARY KEY,
    EmployeeName TEXT,
    DepartmentID INTEGER,
    Salary INTEGER,
    HireDate DATE,
    ManagerID INTEGER,

    FOREIGN KEY(DepartmentID)
        REFERENCES Departments(DepartmentID)
)

""")

# ----------------------------
# Projects
# ----------------------------

cursor.execute("""

CREATE TABLE Projects(
    ProjectID INTEGER PRIMARY KEY,
    ProjectName TEXT,
    Budget INTEGER
)

""")

# ----------------------------
# Employee_Project
# ----------------------------

cursor.execute("""

CREATE TABLE Employee_Project(
    EmployeeID INTEGER,
    ProjectID INTEGER,

    FOREIGN KEY(EmployeeID)
        REFERENCES Employees(EmployeeID),

    FOREIGN KEY(ProjectID)
        REFERENCES Projects(ProjectID)
)

""")

conn.commit()

print("Tables Created Successfully")

conn.close()