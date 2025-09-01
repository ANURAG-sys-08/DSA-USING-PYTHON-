# Problem Description

# Question 0: Class for Bank Account
#  """ Design a Python class named `BankAccount` to represent bank accounts. 
# Theory: A bank account typically includes attributes such as account number, balance, and account holder name. The class should handle operations such as deposit, withdrawal, and transfer of funds between accounts. 
# Operations: 1. Deposit: Add funds to the account 2. Withdrawal: Subtract funds from the account 3. Transfer: Transfer funds from one account to another Test Cases: 
# Test Case 1: 
# acc1 = BankAccount("John Doe", 1000) 
# acc2 = BankAccount("Jane Smith", 2000) 
# assert acc1.balance == 1000 
# assert acc2.balance == 2000 
# acc1.deposit(500) 
# acc2.withdraw(100)
#  acc1.transfer(acc2, 200) 
# assert acc1.balance == 1300 
# assert acc2.balance == 2100 


class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder_name = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit money should be greater then zero")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("No enough money")
        elif amount <= 0:
            raise ValueError("Deposit money should be greater then zero")
        else:
            self.balance -= amount

    def transfer(self, other_account, amount):
        if amount > self.balance:
            raise ValueError("No enough money")
        elif amount <= 0:
            raise ValueError("Transfer money should be greater then zero")
        else:
            self.balance -= amount
            other_account.balance += amount


acc1 = BankAccount("John Doe", 1000) 
acc2 = BankAccount("Jane Smith", 2000) 
assert acc1.balance == 1000 
assert acc2.balance == 2000 
acc1.deposit(500) 
acc2.withdraw(100)
acc1.transfer(acc2, 200) 
assert acc1.balance == 1300 
assert acc2.balance == 2100 
