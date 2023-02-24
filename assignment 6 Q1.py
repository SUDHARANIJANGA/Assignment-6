import json

class Employee:
    def _init_(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def _str_(self):
        return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"

# Open and read the JSON file
with open("employee.json", "r") as f:
    data = json.load(f)

# Create a list of Employee objects
employees = []
for employee in data:
    emp = Employee(employee["Name"], employee["DOB"], employee["Height"], employee["City"], employee["State"])
    employees.append(emp)

# Print the list of Employee objects
for emp in employees:
    print(emp)