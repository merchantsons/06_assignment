# 1. Using self by merchantsons

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

# Example usage:
student = Student("Alice", 85)
student.display()
