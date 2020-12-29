class Bank_balance:
    def __init__(self, opening_balance):
        self.balance = opening_balance

    def deposit(self, add_money):
        self.balance = self.balance + add_money
        return self.balance

    def withdraw(self, withdraw_money):
        self.balance = self.balance - withdraw_money
        return self.balance


B1 = Bank_balance(1000)

B1.deposit(100)


B1.withdraw(50)

print(B1.balance)
