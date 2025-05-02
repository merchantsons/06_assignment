# 14. Aggregation by merchantsons

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

# Example usage:
emp1 = Employee("Alice")
emp2 = Employee("Bob")
department = Department("Engineering", [emp1, emp2])
print(department.employees[0].name)  # Output: Alice
