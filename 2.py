# 2. Using cls by merchantsons

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Example usage:
obj1 = Counter()
obj2 = Counter()
print(Counter.get_count())  # Output: 2
