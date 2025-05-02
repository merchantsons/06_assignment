# 8. The super() Function by merchantsons

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Example usage:
teacher = Teacher("Charlie", "Math")
print(teacher.name)    # Output: Charlie
print(teacher.subject) # Output: Math
