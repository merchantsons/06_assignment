# 18. Property Decorators: @property, @setter, and @deleter by merchantsons

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Price must be positive")

    @price.deleter
    def price(self):
        del self._price

# Example usage:
product = Product(100)
print(product.price)  # Output: 100
product.price = 150
print(product.price)  # Output: 150
del product.price
# print(product.price)  # AttributeError: 'Product' object has no attribute '_price'
