from abc import ABC, abstractmethod
from validations import Validations  # Make sure you import your Validations class

class RideSharingOperations(ABC):
    @abstractmethod
    def request_ride(self, passenger, destination):
        pass

    @abstractmethod
    def accept_ride(self, driver, ride):
        pass

    @abstractmethod
    def complete_ride(self, driver, ride):
        pass

class Vehicle(ABC):
    @abstractmethod
    def get_vehicle_type(self):
        pass

class Car(Vehicle):
    def get_vehicle_type(self):
        return "Car"

class Motorcycle(Vehicle):
    def get_vehicle_type(self):
        return "Motorcycle"

class Driver:
    def __init__(self, name, contact_info, vehicle):
        self.__name = None
        self.__contact_info = None
        self.__vehicle = None
        self.__rides = []
        self.__ratings = []

        self.name = name
        self.contact_info = contact_info
        self.vehicle = vehicle

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if Validations.is_valid_name(value):
            self.__name = value
        else:
            print("Invalid name format.")

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if Validations.is_valid_email(value):
            self.__contact_info = value
        else:
            print("Invalid email format.")

    @property
    def vehicle(self):
        return self.__vehicle

    @vehicle.setter
    def vehicle(self, value):
        if isinstance(value, Vehicle):
            self.__vehicle = value
        else:
            print("Invalid vehicle type.")

    @property
    def rides(self):
        return self.__rides

    @property
    def ratings(self):
        return self.__ratings

    def accept_ride(self, ride):
        if isinstance(ride, Ride):
            self.__rides.append(ride)
            return ride
        else:
            print("Invalid ride format.")

    def complete_ride(self, ride):
        if ride in self.__rides:
            self.__rides.remove(ride)
        else:
            print("This ride is not associated with the driver.")

    def rate_passenger(self, ride, rating):
        if ride in self.__rides:
            passenger = ride.passenger
            if isinstance(rating, int):
                passenger.receive_rating(rating)
            else:
                print("Invalid rating value.")
        else:
            print("This ride is not associated with the driver.")

class Passenger:
    def __init__(self, name, contact_info):
        self._name = None
        self._contact_info = None
        self._rides = []
        self._ratings = []

        self.name = name
        self.contact_info = contact_info

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if Validations.is_valid_name(value):
            self.__name = value
        else:
            print("Invalid name format.")

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if Validations.is_valid_email(value):
            self.__contact_info = value
        else:
            print("Invalid email format.")

    @property
    def rides(self):
        return self.__rides

    @property
    def ratings(self):
        return self.__ratings

    def request_ride(self, driver, destination):
        if isinstance(destination, str) and isinstance(driver, Driver):
            ride = Ride(driver, self, destination)
            driver.accept_ride(ride)
            self.__rides.append(ride)
            return ride
        else:
            print("Invalid ride request format.")

    def receive_rating(self, rating):
        if Validations.is_valid_rating(rating):
            self.__ratings.append(rating)
        else:
            print("Invalid rating value.")

class Ride:
    def __init__(self, driver, passenger, destination):
        self.__driver = None
        self.__passenger = None
        self.__destination = None
        self.__fare = None

        self.driver = driver
        self.passenger = passenger
        self.destination = destination

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, value):
        if isinstance(value, Driver):
            self.__driver = value
        else:
            print("Invalid driver format.")

    @property
    def passenger(self):
        return self.__passenger

    @passenger.setter
    def passenger(self, value):
        if isinstance(value, Passenger):
            self.__passenger = value
        else:
            print("Invalid passenger format.")

    @property
    def destination(self):
        return self.__destination

car = Car()
driver1 = Driver("Driver 1", "driver1@example.com", car)
passenger1 = Passenger("Passenger 1", "passenger1@example.com")

ride1 = passenger1.request_ride(driver1, "Downtown")
driver1.accept_ride(ride1)
ride1.calculate_fare(10)
driver1.complete_ride(ride1)
passenger1.rate_driver(ride1, 5)

print(f"{passenger1.get_name()}'s rides:")
for ride in passenger1.rides:
    print(f"Destination: {ride.get_destination()}, Fare: {ride.fare}")

print(f"{driver1.get_name()}'s rides:")
for ride in driver1.rides:
    print(f"Destination: {ride.get_destination()}, Fare: {ride.fare}")

print(f"{driver1.get_name()}'s ratings:")
for rating in driver1.ratings:
    print(f"Rating: {rating}")

print(f"{passenger1.get_name()}'s ratings:")
for rating in passenger1.ratings:
    print(f"Rating: {rating}")