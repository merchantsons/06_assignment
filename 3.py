# 3. Public Variables and Methods by merchantsons

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")

# Example usage:
car = Car("Toyota")
print(car.brand)  # Output: Toyota
car.start()       # Output: Toyota car started.
