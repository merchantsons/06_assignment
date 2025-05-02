# 7. Access Modifiers: Public, Private, and Protected by merchantsons

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

# Example usage:
emp = Employee("Bob", 50000, "123-45-6789")
print(emp.name)     # Output: Bob
print(emp._salary)  # Output: 50000 (Accessible but not recommended)
# print(emp.__ssn)  # AttributeError: 'Employee' object has no attribute '__ssn'
