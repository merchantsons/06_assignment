# 19. callable() and __call__() by merchantsons

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Example usage:
multiplier = Multiplier(3)
print(callable(multiplier))  # Output: True
print(multiplier(5))         # Output: 15
