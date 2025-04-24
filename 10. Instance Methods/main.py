class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} is of {self.breed} breed. Woof!"
    
my_dog = Dog("dog", "Labrador")
print(my_dog.bark())