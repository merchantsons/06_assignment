# 21. Make a Custom Class Iterable by merchantsons

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

# Example usage:
countdown = Countdown(3)
for number in countdown:
    print(number)
# Output:
# 3
# 2
# 1
