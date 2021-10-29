import csv

# Create Python scripts to read in user input for Employees, Addresses, and Departments
#   - The Manager should also be an employee
#   - BONUS: Make sure that Address, Department, and Manager ID exist before accepting Employee input
#   - Each Python Script should output data as CSV
#   - Export Departments as a YAML file
#   - BONUS: Export Addresses as a YAML file, grouped by state, and then grouped by city

# - employees:
#   - id
#   - name
#   - age
#   - salary
#   - department id
#   - address id
#   - manager id
# - address:
#   - id
#   - street
#   - city
#   - state
# - department:
#   - id
#   - name
#   - manager id
#   - headquarters address id


employee_list = []

num_emps = int(input("Enter how many employee's will be recorded: "))


for x in range(num_emps):
    while True:
        try:
            id = int(input("Enter employee's ID number: "))
            name = input("Enter employee's full name, separated by a whitespace: ").split()
            first_name = name[0]
            last_name = name[1]
            age = int(input("Enter employee's age: "))
            salary = int(input("Enter employee's salary"))
            department = input("Enter employee's department ID: ")
            address = int(input("Enter employee's adress ID: "))
            manager = int(input("Enter employee's manager ID: "))
        except ValueError: print("Please enter valid value type.")
        else:
            print("Employee succesfully added.")
            break

    employee = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "address": address,
        "manager": manager,
        "department": department,
        "salary": salary
    }

    employee_list.append(employee)

fields = ['id', 'first_name', 'last_name', 'age', 'address_id', 'manager_id', 'department_id', 'salary']

with open("employee_01.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields) 
    writer.writeheader()
    writer.writerows(employee_list) 