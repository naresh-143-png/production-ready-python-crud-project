from db_connection import DatabaseConnection
from mysql.connector import Error
import logging

class Employee:

    def __init__(self):

        self.db = DatabaseConnection()

        self.connection = self.db.connect()

        self.cursor = self.connection.cursor()

    # Insert Employee
    def insert_employee(self, emp_id, emp_name, salary, department):

        try:

            query = """
                    INSERT INTO employees
                    (emp_id, emp_name, salary, department)
                    VALUES (%s, %s, %s, %s)
                    """

            values = (emp_id, emp_name, salary, department)

            self.cursor.execute(query, values)

            self.connection.commit()

            logging.info("Employee inserted successfully")

        except Error as e:

            self.connection.rollback()

            logging.error(f"Insert Error: {e}")

    # Update Employee
    def update_employee(self, emp_id, salary, department):

        try:

            query = """
                    UPDATE employees
                    SET salary = %s,
                        department = %s
                    WHERE emp_id = %s
                    """

            values = (salary, department, emp_id)

            self.cursor.execute(query, values)

            self.connection.commit()

            logging.info("Employee updated successfully")

        except Error as e:

            self.connection.rollback()

            logging.error(f"Update Error: {e}")

    # Delete Employee
    def delete_employee(self, emp_id):

        try:

            query = """
                    DELETE FROM employees
                    WHERE emp_id = %s
                    """

            self.cursor.execute(query, (emp_id,))

            self.connection.commit()

            logging.info("Employee deleted successfully")

        except Error as e:

            self.connection.rollback()

            logging.error(f"Delete Error: {e}")

    # Fetch Employees
    def fetch_employees(self):

        try:

            query = "SELECT * FROM employees"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records:
                print(row)

        except Error as e:

            logging.error(f"Fetch Error: {e}")

    # Close Connection
    def close_connection(self):

        if self.cursor:
            self.cursor.close()

        self.db.close_connection()