# 4. Class Variables and Class Methods by merchantsons

class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example usage:
print(Bank.bank_name)  # Output: Default Bank
Bank.change_bank_name("New Bank")
print(Bank.bank_name)  # Output: New Bank
