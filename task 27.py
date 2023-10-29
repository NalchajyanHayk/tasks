from validations import Validations
from abc import ABC, abstractmethod

class BankingOperations(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, to_account, amount):
        pass
class Account:
    def __init__(self, account_type, balance=0):
        self._account_type = None
        self._balance = None
        self._account_number = None
        self._transactions = []

        self.account_type = account_type
        self.balance = balance
        self.account_number = self.generate_account_number()

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        if Validations.checking_account(value):
            self._account_type = value
        else:
            print("Invalid account type.")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if Validations.is_positive_number(value):
            self._balance = value
        else:
            print("Invalid balance.")

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        if value is not None:
            self._account_number = value
        else:
            print("Invalid account number.")

    @property
    def transactions(self):
        return self._transactions

    def generate_account_number(self):
        # Generate a unique account number (you can implement your own logic here)
        return "ACC123456"

    def deposit(self, amount):
        if Validations.is_positive_number(amount):
            self._balance += amount
            self._transactions.append(f"Deposit: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if Validations.is_positive_number(amount) and self.balance >= amount:
            self._balance -= amount
            self._transactions.append(f"Withdrawal: {amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def transfer(self, to_account, amount):
        if Validations.is_positive_number(amount) and self.balance >= amount:
            self._balance -= amount
            self._transactions.append(f"Transfer to {to_account.account_number}: {amount}")
            to_account.deposit(amount)
        else:
            print("Invalid transfer amount or insufficient balance.")

class Customer:
    def __init__(self, name, contact_info):
        self._name = None
        self._contact_info = None
        self._accounts = []

        self.name = name
        self.contact_info = contact_info

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if Validations.is_valid_name(value):
            self._name = value
        else:
            print("Invalid name format.")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if Validations.is_valid_email(value):
            self._contact_info = value
        else:
            print("Invalid email format.")

    @property
    def accounts(self):
        return self._accounts

    def add_account(self, account):
        if isinstance(account, Account):
            self._accounts.append(account)
        else:
            print("Invalid account.")


# Instantiate a customer and two accounts
customer = Customer("Alice", "alice@example.com")
account1 = Account("Savings", 1000)
account2 = Account("Checking", 500)  # Set an initial balance for account2

# Add the accounts to the customer
customer.add_account(account1)
customer.add_account(account2)

# Perform transactions
account1.deposit(500)
account1.withdraw(200)
account1.transfer(account2, 300)

# View account balances and transaction history
for account in customer.accounts:
    print(f"Account Type: {account.account_type}")
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print("Transaction History:")
    for transaction in account.transactions:
        print(f"- {transaction}")
