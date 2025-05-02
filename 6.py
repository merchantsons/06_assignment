# 6. Constructors and Destructors by merchantsons

class Logger:
    def __init__(self):
        print("Logger created.")

    def __del__(self):
        print("Logger destroyed.")

# Example usage:
logger = Logger()
del logger  # Output: Logger destroyed.
