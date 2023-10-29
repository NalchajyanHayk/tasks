from re import findall
from validations import Validations
class Customer:
    def __init__(self, name, contact_info):
        self._name = None
        self._contact_info = None
        self._past_orders = []
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
    def past_orders(self):
        return self._past_orders

    def create_order(self, products):
        if isinstance(products, list):
            order = Order(self, products)
            self._past_orders.append(order)
            return order
        else:
            print("Invalid order format.")

class Product:
    def __init__(self, name, description, price, availability):
        self._name = None
        self._description = None
        self._price = None
        self._availability = None
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability

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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if Validations.is_positive_number(value):
            self._price = value
        else:
            print("Invalid price format.")

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, value):
        self._availability = value

class Order:
    def __init__(self, customer, products):
        self._customer = None
        self._products = []
        self._total = 0
        self.customer = customer
        self.products = products

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        self._customer = value

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        if isinstance(value, list):
            self._products = value
            self._total = sum(product.price for product in value)
        else:
            print("Invalid products format.")

    @property
    def total(self):
        return self._total

# Example usage:
customer = Customer("Alice", "alice@example.com")
product1 = Product("Laptop", "High-performance laptop", 1000, 10)
product2 = Product("T-shirt", "Comfortable cotton t-shirt", 20, 50)
order = customer.create_order([product1, product2])
print(f"{customer.name}'s orders:")
for o in customer.past_orders:
    print(f"Total: ${o.total}")
