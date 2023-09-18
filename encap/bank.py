class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance


# Create a bank account
account1 = BankAccount("Alice", 1000)

# Deposit and withdraw money
account1.deposit(500)
account1.withdraw(200)

# Access the balance using the getter method
print("Current Balance:", account1.get_balance())
