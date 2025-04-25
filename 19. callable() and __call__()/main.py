# In Python, callable() is a built-in function that checks if an object can be called (i.e., used with parentheses like a function). 
# It returns True if the object is callable and False otherwise. 
# Functions, methods, classes, and instances of classes with a __call__() method are all examples of callable objects. 

# The __call__() method is a special method in Python classes that allows instances of the class to be called like functions. 
# When an instance of a class with a __call__() method is called, the __call__() method is executed. 
# This enables objects to behave like functions, encapsulating state and behavior within them.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor
    
double = Multiplier(5)
triple = Multiplier(5)

print(callable(double))
print(callable(triple))

print(double(2))
print(triple(3))