# Write a program that simulates a banking system. The program should have classes for
# customers, accounts, and transactions. Customers should have attributes such as name,
# address, and contact information. Accounts should have attributes such as account type,
# balance, and interest rate. Transactions should have attributes such as the account involved,
# the transaction type, and the amount of the transaction. Use inheritance to implement classes for
# different types of accounts (e.g., savings, checking) and abstract classes for account operations.
from validations import Validations
from abc import ABC, abstractmethod

validating = Validations()

class Customer:
    def __init__(self, name, address, contact_info):
        self._name = name
        self._address = address
        self._contact_info = contact_info


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if validating._is_valid_name(new_name):
            self._name = new_name
        else:
            raise ValueError("Invalid name format")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        if validating._is_valid_address(new_address):
            self._address = new_address
        else:
            raise ValueError("Invalid address format")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, new_contact_info):
        if validating._is_valid_phone_number(new_contact_info):
            self._contact_info = new_contact_info
        else:
            raise ValueError("Invalid phone number format")

class Account(ABC):
    def __init__(self, account_type, balance, interest_rate):
        try:
            if validating.checking_account(account_type) and validating.count_digits_and_check(balance, 16) and validating.count_digits_and_check(interest_rate, 2):
                self._account_type = account_type
                self._balance = balance
                self._interest_rate = interest_rate
            else:
                raise Exception ("impossible to create an object")
        except Exception as e:
            print(e)

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, new_account_type):
        if validating.checking_account(new_account_type):
            self._account_type = new_account_type
        else:
            raise ValueError("Invalid account type")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if validating.count_digits_and_check(new_balance, 16):
            self._balance = new_balance
        else:
            raise ValueError("Invalid balance format")

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, new_interest_rate):
        if validating.count_digits_and_check(new_interest_rate, 2):
            self._interest_rate = new_interest_rate
        else:
            raise ValueError("Invalid interest rate format")

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

class AccountOperations(ABC):
    @abstractmethod
    def transfer(self, amount, target_account):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def account_statement(self):
        pass

class SavingsAccount(Account, AccountOperations):
    def __init__(self, name, address, contact_info):
        super().__init__(name, address, contact_info)


    def deposit(self, amount):
        if type(amount) == eval and amount > 0:
            self._balance += amount
        else:
            print("sth wrong with the input!")

    def withdraw(self, amount):
        if type(amount) == eval:
            if amount <= self._balance:
                self._balance -= amount
            else:
                print("Insufficient funds.")
        else:
            print("sth wrong with the input!")

    def calculate_interest(self):
        return self._balance * (self._interest_rate / 100)

    def transfer(self, amount, target_account):
        if amount <= self._balance:
            self._balance -= amount
            target_account.deposit(amount)
        else:
            print("Insufficient funds for transfer.")

    def check_balance(self):
        pass

    def account_statement(self):
        return f"Account Type: {self._account_type}\nBalance: {self._balance}"

class CheckingAccount(Account, AccountOperations):
    def deposit(self, amount):
        if type(amount) == eval and amount > 0:
            self._balance += amount
        else:
            print("sth wrong with the input!")

    def withdraw(self, amount):
        if type(amount) == eval:
            if amount <= self._balance:
                self._balance -= amount
            else:
                print("Insufficient funds.")
        else:
            print("sth wrong with the input!")

    def calculate_interest(self):
        return 0  # Checking accounts typically don't earn interest

    def transfer(self, amount, target_account):
        if type(amount) == eval and type(target_account) == Account:
            if 0 < amount <= self._balance:
                self._balance -= amount
                target_account.deposit(amount)
            else:
                print("Insufficient funds for transfer.")
        else:
            print("sth wrong with the input!")

    def check_balance(self):
        return self._balance

    def account_statement(self):
        return f"Account Type: {self._account_type}\nBalance: {self._balance}"


class Transaction:
    def __init__(self, account, transaction_type, amount):
        self._transaction_type =transaction_type
        self._amount = amount
        self._account = account

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, new_transaction_type):
        if validating.transaction_checking(new_transaction_type):
            self._transaction_type = new_transaction_type
        else:
            raise ValueError("Invalid transaction type")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        if isinstance(new_amount, (int, float)):
            self._amount = new_amount
        else:
            raise ValueError("Amount must be an integer or float")

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, new_account):
        if validating.type_checking(new_account, Account):
            self._account = new_account
        else:
            raise ValueError("Invalid account type")




