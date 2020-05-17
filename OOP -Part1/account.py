class Account:

    # Constructor function
    def __init__(self, number, owner, balance, limit):
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def view_balance(self):
        print("Current balance is {} for {}'s account".format(self.balance, self.owner))

    def deposit(self, valor):
        self.balance += valor

    def withdraw(self, valor):
        self.balance -= valor
