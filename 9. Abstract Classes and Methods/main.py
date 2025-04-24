# Importing ABC and abstractmethod from abc module. ABC is an abstract base class and abstractmethod is a decorator that is used to define an abstract method.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self, length, width):
        pass

class Rectangle(Shape):
    def area(self, length, width):
        return length * width 

rec = Rectangle() # Instantiating the class Rectangle() and storing it in rec variable.
area = rec.area(10, 20) # Calling the area method on rec object and passing length and width as arguments.
print(area)

def calculate_area(shape: Shape, length, width):
    return shape.area(length, width)

print(calculate_area(Rectangle(), 10, 20))
