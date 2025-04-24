# Composition = The composed object directly owns its components, which cannot exist independently
# "owns-a" relationship 

class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self):
        self.engine = Engine() # Composition: Car owns an Engine.

my_car = Car()
print(my_car.engine.start())