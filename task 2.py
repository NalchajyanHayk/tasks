# Write a program that simulates a car dealership system. The program should have classes for cars,
# customers, and salespeople. Cars should have attributes such as make, model, and price. Customers should have
# attributes such as name and contact information. Salespeople should have attributes such as name and commission rate.
# The program should allow salespeople to manage car inventory, customers to search for and purchase cars,
# and salespeople to view their sales history. Use interfaces to implement classes for different types of cars
# (e.g., electric, hybrid) and abstract classes for sales operations.

from abc import ABC, abstractmethod
from validations import Validations

valid = Validations()


class Car(ABC):
    def __init__(self, make, model, price):
        self._make = make
        self._model = model
        self._price = price


    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, new_make):
        if valid.make_valid(new_make):
            self._make = new_make
        else:
            raise ValueError("Invalid make format")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        if valid.car_model_valid(new_model):
            self._model = new_model
        else:
            raise ValueError("Invalid car model format")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if  isinstance(new_price, int) and new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Price must be a positive number")

    @abstractmethod
    def intro(self):
        pass


class Electric(Car):
    def __init__(self, make, model, price):
        super().__init__(make, model, price)

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, new_make):
        if valid.make_valid(new_make):
            self._make = new_make
        else:
            raise ValueError("Invalid make format")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        if valid.car_model_valid(new_model):
            self._model = new_model
        else:
            raise ValueError("Invalid car model format")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int) and new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Price must be a positive number")

    def intro(self):
        print("here is the intro of this electric car:")
        print(f"{self._model}: ${self._price}")


class Hybrid(Car):
    def __init__(self, make, model, price):
        super().__init__(make, model, price)

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, new_make):
        if valid.make_valid(new_make):
            self._make = new_make
        else:
            raise ValueError("Invalid make format")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        if valid.car_model_valid(new_model):
            self._model = new_model
        else:
            raise ValueError("Invalid car model format")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int) and new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Price must be a positive number")

    def intro(self):
        print("here is the intro of this hybrid car:")
        print(f"{self._model}: ${self._price}")


class Customer:
    def __init__(self, name, contact_info):
        self._name = name
        self._contact_info = contact_info

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if valid._is_valid_name(new_name):
            self._name = new_name
        else:
            raise ValueError("Invalid name format")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, new_contact_info):
        if valid._is_valid_phone_number(new_contact_info):
            self._contact_info = new_contact_info
        else:
            raise ValueError("Invalid phone number format")

# class Saleperson:
#     def __init__(self, name, commision_rate):
