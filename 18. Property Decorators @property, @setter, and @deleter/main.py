class Product:
    def __init__(self, price) -> None:
        self.__price = price

    @property
    def price(self) -> int | float:
        try:
            return self.__price
        except AttributeError:
            print("Please set a price first.")
    
    @price.setter
    def price(self, new_price) -> None:
        if new_price > 0 and isinstance(new_price, (int, float)):
            self.__price = new_price
        else:
            print("Please enter a valid price")
    
    @price.deleter
    def price(self) -> None:
        del self.__price


product = Product(10)
print(product.price)
product.price = 20
print(product.price)
del product.price
print(product.price)