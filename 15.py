# 15. Method Resolution Order (MRO) and Diamond Inheritance by merchantsons

class A:
    def show(self):
        print("A show")

class B(A):
    def show(self):
        print("B show")

class C(A):
    def show(self):
        print("C show")

class D(B, C):
    pass

# Example usage:
d = D()
d.show()  # Output: B show (due to MRO)
