from abc import ABC, abstractmethod
from validations import Validations

class Product(ABC):
    def __init__(self, name, price, description):
        self._name = name
        self._price = price
        self._description = description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if Validations.is_valid_name(value):
            self._name = value
        else:
            print("invalid input")
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, int) and value > 0:
            self._price = value
        else:
            print("invalid input")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if Validations.has_more_than_10_words(value):
            self._description = value
        else:
            print("Invalid value")

    @abstractmethod
    def display_product_info(self):
        pass

class Electronics(Product):
    def __init__(self, name, price, description, brand):
        super().__init__(name, price, description)
        self._brand = brand

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if Validations.is_valid_name(value):
            self._brand = value
        else:
            print("invalid brand")

    def display_product_info(self):
        super().display_product_info()
        print(f"Brand: {self.brand}")


class Clothing(Product):
    def __init__(self, name, price, description, size):
        super().__init__(name, price, description)
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value > 0:
            self._size = value
        else:
            print("invalid size")

    def display_product_info(self):
        super().display_product_info()
        print(f"Size: {self.size}")


class Customer:
    def __init__(self, name, contact_info):
        self._name = name
        self._contact_info = contact_info
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if Validations.is_valid_name(value):
            self._name = value
        else:
            print("invalid input")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if Validations.is_valid_email(value):
            self._contact_info = value
        else:
            print("invalid input")

    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, value):
        if isinstance(value, Order):
            self._orders = value
        else:
            print("invalid input")

    def purchase_product(self, product):
        if isinstance(product, Product):
            order = Order(self, product)
            self._orders.append(order)
            return order
        else:
            print("invalid input")

    def view_order_history(self):
        print(f"Order history for {self.name}:")
        for order in self._orders:
            order.display_order_info()

    def leave_review(self, product, review):
        if isinstance(product, Product) and Validations.has_more_than_10_words(review):
            print(f"Review for {product.name} by {self.name}:")
            print(review)
        else:
            print("try again")


class Order:
    def __init__(self, customer, product):
        self._customer = customer
        self._products = [product]
        self._total_price = product.price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if type(value) == Customer:
            self._customer = value
        else:
            print("invalid customer")

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        self._products = value

    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        if type(value) == int and value > 0:
            self._total_price = value
        else:
            print("invalid value")

    def add_product(self, product):
        if type(product) == Product:
            self._products.append(product)
            self._total_price += product.price
        else:
            print("invalid product")

    def display_order_info(self):
        print("Order details:")
        for product in self._products:
            product.display_product_info()
        print(f"Total Price: ${self.total_price}\n")


product1 = Electronics("Smartphone", 500, "High quality smartphone", "Samsung")
product2 = Clothing("Jeans", 30, "Blue jeans", 56)

customer1 = Customer("Alice", "alice@example.com")
customer2 = Customer("Bob", "bob@example.com")

order1 = Order(customer1, product1)
order2 = Order(customer2, product2)

customer1.purchase_product(product1)
customer2.purchase_product(product2)

order1.add_product(product2)

customer1.leave_review(product1, "Great smartphone for the price!")

