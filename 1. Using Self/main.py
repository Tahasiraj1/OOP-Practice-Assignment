class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        return f"Name: {self.name}, Marks: {self.marks}"


Taha = Student('Taha', 90)
print(Taha.display())