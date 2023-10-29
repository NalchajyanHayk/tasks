from abc import ABC, abstractmethod
from validations import Validations
from datetime import datetime, timedelta

Validations = Validations()

class RentalOperation(ABC):
    @abstractmethod
    def search_cars(self):
        pass

    @abstractmethod
    def rent_car(self, car, customer, rental_duration):
        pass

    @abstractmethod
    def return_car(self, rental):
        pass

class CarType(ABC):
    @abstractmethod
    def get_rental_price(self):
        pass

class LuxuryCar(CarType):
    def get_rental_price(self):
        return 100

class EconomyCar(CarType):
    def get_rental_price(self):
        return 50


class Car:
    def __init__(self, make, model, car_type):
        self._make = make
        self._model = model
        self._car_type = car_type

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        if isinstance(make, str) and make:
            self._make = make
        else:
            raise ValueError("Make must be a non-empty string")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and model:
            self._model = model
        else:
            raise ValueError("Model must be a non-empty string")

    @property
    def car_type(self):
        return self._car_type

class Customer:
    def __init__(self, name, contact_info):
        self._name = name
        self._contact_info = contact_info
        self._rental_history = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        if isinstance(contact_info, str) and contact_info:
            self._contact_info = contact_info
        else:
            raise ValueError("Contact information must be a non-empty string")

    @property
    def rental_history(self):
        return self._rental_history

    def add_rental(self, rental):
        if isinstance(rental, Rental):
            self._rental_history.append(rental)
        else:
            raise ValueError("Invalid rental object")

    def view_rental_history(self):
        return self._rental_history

class Rental:
    def __init__(self, customer, car, rental_duration, rental_price):
        self._customer = customer
        self._car = car
        self._rental_duration = rental_duration
        self._rental_price = rental_price
        self._rental_date = datetime.now()


    @property
    def customer(self):
        return self._customer

    @property
    def car(self):
        return self._car

    @property
    def rental_duration(self):
        return self._rental_duration

    @rental_duration.setter
    def rental_duration(self, rental_duration):
        if isinstance(rental_duration, int) and rental_duration > 0:
            self._rental_duration = rental_duration
        else:
            raise ValueError("Rental duration must be a positive integer")

    @property
    def rental_price(self):
        return self._rental_price

    @property
    def rental_date(self):
        return self._rental_date

    def return_car(self):
        return_date = datetime.now()
        days_rented = (return_date - self._rental_date).days
        if days_rented < self._rental_duration:
            self._rental_duration = days_rented
        return self._rental_price



luxury_car = LuxuryCar()
economy_car = EconomyCar()

car = Car("BMW", "sedan", luxury_car)


customer = Customer("John Doe", "john.doe@example.com")
rental = Rental(customer, car, 7, rental_price=700)

customer.add_rental(rental)

rental_history = customer.view_rental_history()


