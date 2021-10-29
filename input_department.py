import csv
import yaml

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

dept_list = []

num_dept = int(input("Enter how many departments will be recorded: "))


for x in range(num_dept):
    while True:
        try:
            id = int(input("Enter department's ID number: "))
            name = input("Enter the department's name: ")
            manager_id = input("Enter the manager's ID: ")
            headquarters_id = input("Enter the headquarters' address ID: ")
        except ValueError: print("Please enter valid value type.")
        else:
            print("Department succesfully added.")
            break

    department = {
        "id": id,
        "name": name,
        "manager_id": manager_id,
        "headquarters_id": headquarters_id
    }

    dept_list.append(department)

fields = ['id', 'name', 'manager_id', 'headquarters_id']

with open("department_01.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields) 
    writer.writeheader()
    writer.writerows(dept_list)

with open('department_01.yaml', 'w') as outfile_y:
    for x in dept_list:
        yaml.dump(x, outfile_y) 