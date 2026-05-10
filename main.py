
from employee_service import Employee
import logging

def main():

    emp = Employee()

    while True:

        print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
        print("1. Insert Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Fetch Employees")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        # Insert Employee
        if choice == '1':

            try:
                emp_id = int(input("Enter Employee ID: "))
                emp_name = input("Enter Employee Name: ")
                salary = float(input("Enter Salary: "))
                department = input("Enter Department: ")

                emp.insert_employee(
                    emp_id,
                    emp_name,
                    salary,
                    department
                )

            except ValueError:
                logging.error("Invalid Input! Please enter correct data types.")

        # Update Employee
        elif choice == '2':

            try:
                emp_id = int(input("Enter Employee ID to Update: "))
                salary = float(input("Enter New Salary: "))
                department = input("Enter New Department: ")

                emp.update_employee(
                    emp_id,
                    salary,
                    department
                )

            except ValueError:
                logging.error("Invalid Input! Please enter correct data types.")

        # Delete Employee
        elif choice == '3':

            try:
                emp_id = int(input("Enter Employee ID to Delete: "))

                emp.delete_employee(emp_id)

            except ValueError:
                logging.error("Invalid Employee ID")

        # Fetch Employees
        elif choice == '4':

            emp.fetch_employees()

        # Exit
        elif choice == '5':

            print("\nClosing Application...")

            emp.close_connection()

            break

        else:
            print("\nInvalid Choice! Please select between 1 to 5")


# Main Driver
if __name__ == "__main__":

    main()