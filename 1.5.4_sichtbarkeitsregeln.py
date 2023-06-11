class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # public variable
        self._balance = balance               # protected variable
        self.__pin = "9988"                   # private variable

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        self._balance = amount

    def get_pin(self):
        return self.__pin

my_account = BankAccount("111222333444", 2000)

print(my_account.account_number)            # Output: 111222333444
print(my_account.get_balance())             # Output: 2000

my_account.set_balance(2200)
print(my_account.get_balance())             # Output: 2200

print(my_account.get_pin())                 # Output: 9988
print(my_account.__pin)                     # Error: AttributeError: 'BankAccount' object has no attribute '__pin'
