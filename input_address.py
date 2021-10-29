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

address_list = []

num_address = int(input("Enter how many addresses will be recorded: "))


for x in range(num_address):
    while True:
        try:
            id = int(input("Enter address's ID number: "))
            street = input("Enter the street name and number: ")
            city = input("Enter the city: ")
            state = input("Enter the state: ")
        except ValueError: print("Please enter valid value type.")
        else:
            print("Address succesfully added.")
            break

    address = {
        "id": id,
        "street": street,
        "city": city,
        "state": state
    }

    address_list.append(address)

fields = ['id', 'street', 'city', 'state']

with open("address_01.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields) 
    writer.writeheader()
    writer.writerows(address_list) 