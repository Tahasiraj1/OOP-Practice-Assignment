class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} is started. Vroom, Vroom!"
    

my_car = Car('BMW')
print(my_car.brand)
print(my_car.start())