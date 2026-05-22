
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def transfer_to(self, other_account, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                other_account.balance += amount
                print(f"Transferred ${amount} to {other_account.name}. New balance: ${self.balance}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Transfer amount must be positive.")

    def info(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance}"