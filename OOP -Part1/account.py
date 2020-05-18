class Account:

    # Constructor function
    def __init__(self, number, owner, balance, limit):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def view_balance(self):
        print("Current balance is {} for {}'s account".format(self.__balance, self.__owner))

    def __can_withdraw(self, value_to_get):
        available_to_get = self.__balance + self.__limit
        return value_to_get <= available_to_get

    def withdraw(self, valor):
        if self.__can_withdraw(valor):
            self.__balance -= valor
        else:
            print("The value {} is over the limit".format(valor))

    def deposit(self, valor):
        self.__balance += valor

    def transfer(self, valor, receiver):
        self.withdraw(valor)
        receiver.deposit(valor)

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def all_bank_codes():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}