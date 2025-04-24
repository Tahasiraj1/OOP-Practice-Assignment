# Aggregation = A relationship where one object contains references to other INDEPENDENT objects
# "has-a" relationship

class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, Department: {self.department.name}"

department = Department("IT")
employee = Employee("Taha", department) # Aggregation: Employee has a Department.

print(employee)