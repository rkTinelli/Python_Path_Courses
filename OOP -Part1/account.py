class Account:

    # Constructor function
    def __init__(self, number, owner, balance, limit):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def view_balance(self):
        print("Current balance is {} for {}'s account".format(self.__balance, self.__owner))

    def deposit(self, valor):
        self.__balance += valor

    def withdraw(self, valor):
        self.__balance -= valor

    def transfer(self, valor, receiver):
        self.withdraw(valor)
        receiver.deposit(valor)
