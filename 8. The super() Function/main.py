class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject 


Sir = Teacher("Taha", "Math")
print(Sir.name, Sir.subject)