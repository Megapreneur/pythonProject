class Account:
    def __init__(self, name):
        self.balance = 0

        self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot deposited")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Amount cannot be withdrawn ")
        self.balance -= amount

    def transfer(self, amount, account_number):
        self.balance -= amount
        account_number.deposit(amount)

    def buy_airtime(self, amount):
        self.balance -= amount
