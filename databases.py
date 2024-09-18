import mysql.connector
connection= mysql.connector.connect(
    user="luoying",
    password="mypassword",
    host="localhost",
    port=3306,
    database="kirpaldb",
    charset="utf8mb4",
    collation= "utf8mb4_general_ci"
    )
print("Connected successfully to MariaDB!")


def get_employees_by_last_name(last_name):
    sql = f"SELECT Number, LastName, FirstName, Salary FROM Employee1 WHERE LastName='{last_name}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Hello! I'm {row[2]} ({row[1]}). My salary is {row[3]} euros per month.")
    else:
        print("No employees found with that last name.")
    return result

# Establish connection to the database
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='kirpaldb',
    user='luoying',
    password='mypassword',
    autocommit=True,
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
    )

last_name = input("Enter last name: ")
get_employees_by_last_name(last_name)

import mysql.connector


def update_salary(number, new_salary):
    # Establishing the database connection
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='kirpaldb',
        user='luoying',
        password='mypassword',
        autocommit=True,
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
        )

    # Create a cursor object
    cursor = connection.cursor()

    # SQL query to update the salary
    sql = "UPDATE Employee1 SET Salary = %s WHERE Number = %s"

    # Executing the query
    cursor.execute(sql, (new_salary, number))

    # Check if the update was successful
    if cursor.rowcount == 1:
        print("Salary updated successfully.")
    else:
        print("No employee1 found with that number.")

    # Closing the connection
    connection.close()


# Getting input from the user
number = int(input("Enter the employee number: "))
new_salary = float(input("Enter the new salary: "))

# Calling the function to update salary
update_salary(number, new_salary)
print(f"My salary is {new_salary} euros per month now.")
