import uuid
import datetime

# Print list of tuples nicely
def print_tuple_list(tup_list):
    for tup in tup_list:
        print('\n'.join(str(x) for x in tup))
        print("---")

class Account():

    # Constructor
    def __init__(self, acc_type):
        # Unique identifier with uuid
        self._acc_number = uuid.uuid4()
        self._acc_type = acc_type
        self._balance = 0.0
        self._transactions = []

    @property
    def acc_number(self):
        return self._acc_number

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    @property
    def transactions(self):
        return self._transactions

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        # Add amount to account balance
        self.balance += amount
        
        # Add transaction to list with datetime
        self.transactions.append((datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Deposit", amount))

    
    def withdraw(self, amount):
        # Check if withdraw amount is more than balance
        if amount > self.balance:
            return "Insufficient funds"
        else:
            # Subtract amount from account balance
            self.balance -= amount

            # Add transaction to list
            self.transactions.append((datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Withdraw", -amount))

    # transfer money from one account to another
    def transfer(self, amount, transfer_account, reference = ""):

        # Check if withdraw amount is more than balance
        if amount > self.balance:
            print("Insufficient funds")
            return False
        else:
            self.balance -= amount
            transfer_account.balance += amount

            # Add transaction to list
            self.transactions.append((datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Transfer", -amount, transfer_account.acc_number, reference))

            print("Transfer successful")

            return True
        
   # get the last n transactions
    def get_transactions(self, n = 10):
        return self.transactions[-n:]
    
    # close account if balance is 0
    def close(self):
        if self.balance == 0:
            print("Account will be closed.")
            return True
        else:
            print("Account can't be closed. Balance is not 0.")
            return False


class Bank():
    
    # Constructor
    def __init__(self):
        self._accounts = {}
        self._transactions = []

    @property
    def accounts(self):
        return self._accounts

    def open_account(self, acc_type):
        new_account = Account(acc_type)

        # Add account to dictionary
        self.accounts[new_account.acc_number] = new_account

        return new_account.acc_number

    def close_account(self, acc_number):
        account = self.find_account(acc_number)
        if isinstance(account, Account) and account.close():
            self.accounts.pop(acc_number)
            print("Account closed successfully.")
        else:
            print("Account closing failed.")
    
    def find_account(self, acc_number):
        if acc_number not in self.accounts:
            return "Account not found" 
        else:
            return self.accounts[acc_number]
        
    def transfer(self, debit_acc_number, credit_acc_number, amount, reference = ""):
        debit_acc = self.find_account(debit_acc_number)
        credit_acc = self.find_account(credit_acc_number)

        if isinstance(debit_acc, Account) and isinstance(credit_acc, Account):
            if debit_acc.transfer(amount, credit_acc, reference):
                self._transactions.append((datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Transfer", -amount, debit_acc.acc_number, credit_acc.acc_number, reference))
                return True
            else:
                return False
        else:
            print("Transfer failed.")
            return False
        
        
# Test
bank = Bank()

# 1. Open accounts
acc1 = bank.open_account("Spendings")
acc2 = bank.open_account("Savings")

# 2. Deposit money
bank.find_account(acc1).deposit(1000)
bank.find_account(acc2).deposit(5000)

# 3. Transfer money
bank.transfer(acc1, acc2, 2000, "Taxes") # insufficient funds
bank.transfer(acc1, acc2, 500, "Rent") # successful
bank.transfer(acc2, acc1, 1500, "Vacation") # successful

# 4. Check balance
print(bank.find_account(acc1).check_balance())
print(bank.find_account(acc2).check_balance())

# 5. Get last 2 transactions
print_tuple_list(bank.find_account(acc1).get_transactions(2))

# 6. Get last 2 transactions from bank
print_tuple_list(bank.find_account(acc2).get_transactions(2))

# 7. Close account
bank.close_account(acc1)

# Show balance 
print(bank.find_account(acc1).check_balance())