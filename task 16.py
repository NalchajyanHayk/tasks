import re
from abc import ABC, abstractmethod
from validations import Validations

class Account(ABC):
    def __init__(self, account_number, balance, account_type):
        self._account_number = account_number
        self._balance = balance
        self._account_type = account_type
        self._transactions = []

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        if Validations.is_valid_name(value):
            self._account_number = value
        else:
            print("Invalid account number format.")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if Validations.is_positive_number(value):
            self._balance = value
        else:
            print("Balance must be a positive number.")

    @property
    def account_type(self):
        return self._account_type

    @property
    def transactions(self):
        return self._transactions

    def deposit(self, amount):
        if Validations.is_positive_number(amount):
            self._balance += amount
            self._transactions.append(Transaction(self, amount, "deposit"))
            print(f"Deposited ${amount} into {self.account_type} account. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if Validations.is_positive_number(amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
                self._transactions.append(Transaction(self, amount, "withdrawal"))
                print(f"Withdrew ${amount} from {self.account_type} account. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def transfer(self, to_account, amount):
        if Validations.is_positive_number(amount):
            if self._balance >= amount:
                self.withdraw(amount)
                to_account.deposit(amount)
                self._transactions.append(Transaction(self, amount, "transfer"))
                print(f"Transferred ${amount} to {to_account.account_type} account. New balance: ${self.balance}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Invalid transfer amount.")

    def view_transaction_history(self):
        print(f"Transaction history for {self.account_type} account (Account Number: {self.account_number}):")
        for transaction in self._transactions:
            transaction.display_transaction_info()

    @abstractmethod
    def display_account_info(self):
        pass

class CheckingAccount(Account):
    def display_account_info(self):
        print(f"Checking Account (Account Number: {self.account_number})\nBalance: ${self.balance}")

class SavingsAccount(Account):
    def display_account_info(self):
        print(f"Savings Account (Account Number: {self.account_number})\nBalance: ${self.balance}")

class Customer:
    def __init__(self, name, contact_info):
        self._name = name
        self._contact_info = contact_info
        self._accounts = []

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

    @accounts.setter
    def accounts(self, value):
        self._accounts = value

    def add_account(self, account):
        if account not in self._accounts:
            self._accounts.append(account)
            print(f"Added {account.account_type} account to customer {self.name}")

    def view_account_info(self):
        print(f"Accounts for customer {self.name}:")
        for account in self._accounts:
            account.display_account_info()

class Transaction:
    def __init__(self, account, amount, transaction_type):
        self._account = account
        self._amount = amount
        self._transaction_type = transaction_type

    @property
    def account(self):
        return self._account

    @property
    def amount(self):
        return self._amount

    @property
    def transaction_type(self):
        return self._transaction_type

    def display_transaction_info(self):
        print(f"{self.transaction_type.capitalize()} of ${self.amount} on {self.account.account_type} account (Account Number: {self.account.account_number})")

# Instantiate the classes
customer1 = Customer("Alice", "alice@email.com")
customer2 = Customer("Bob", "bob@email.com")

checking1 = CheckingAccount("C1001", 1000, "Checking")
savings1 = SavingsAccount("S2001", 5000, "Savings")
checking2 = CheckingAccount("C1002", 2000, "Checking")

customer1.add_account(checking1)
customer1.add_account(savings1)
customer2.add_account(checking2)

checking1.balance = 1500  # Modify the balance using the setter

checking1.deposit(500)
checking1.withdraw(200)
checking1.transfer(savings1, 300)

savings1.deposit(1000)
savings1.withdraw(600)

customer1.view_account_info()
customer2.view_account_info()

checking1.view_transaction_history()
savings1.view_transaction_history()
