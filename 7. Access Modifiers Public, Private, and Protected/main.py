class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

# Instantiating the class
developer = Employee("Taha", '$100000', '123-45-6789')

# Access public attribute
print(developer.name)
# Access protected attribute
print(developer._salary)
# Access the private attribute using name mangling
print(developer._Employee__ssn)

# We can also Access private method using getattr function like this:
print(getattr(developer, '_Employee__ssn'))