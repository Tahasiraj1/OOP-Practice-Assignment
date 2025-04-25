def add_greeting(decorator): # decorator = Person
    def greet(self):
        return "Hello, from decorator!"
    decorator.greet = greet
    return decorator


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

person1 = Person("Taha")
print(person1.greet())