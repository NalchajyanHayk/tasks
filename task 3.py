from abc import ABC, abstractmethod
from validations import Validations


class Dish(ABC):
    def __init__(self, dish_name, dish_price):
        self._dish_name = dish_name
        self._dish_price = dish_price

    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, new_dish_name):
        if Validations.is_valid_name(new_dish_name):
            self._dish_name = new_dish_name
        else:
            raise ValueError("Invalid dish name format")

    @property
    def dish_price(self):
        return self._dish_price

    @dish_price.setter
    def dish_price(self, new_dish_price):
        if isinstance(new_dish_price, (int, float)) and new_dish_price > 0:
            self._dish_price = new_dish_price
        else:
            raise ValueError("Invalid dish price format")


class Appetizer(Dish):
    def __init__(self, dish_name, dish_price):
        super().__init__(dish_name, dish_price)

class Entree(Dish):
    def __init__(self, dish_name, dish_price):
        super().__init__(dish_name, dish_price)


class Menu(ABC):
    def __init__(self):
        self._menu_items = {}

    @abstractmethod
    def add_item(self, dish):
        pass

    @abstractmethod
    def remove_item(self, dish_name):
        pass

    @abstractmethod
    def view_menu(self):
        pass

    @property
    def menu_items(self):
        return self._menu_items

    @menu_items.setter
    def menu_items(self, new_menu_items):
        if isinstance(new_menu_items, dict):
            self._menu_items = new_menu_items
        else:
            raise ValueError("Invalid menu items format")


class Restaurant_Menu(Menu):
    def add_item(self, dish):
        if dish.dish_name not in self._menu_items:
            self._menu_items[dish.dish_name] = dish.dish_price
        else:
            print(f"{dish.dish_name} is already on the menu.")

    def remove_item(self, dish_name):
        if dish_name in self._menu_items:
            del self._menu_items[dish_name]
        else:
            print(f"{dish_name} is not on the menu.")

    def view_menu(self):
        print("Menu:")
        for dish, price in self._menu_items.items():
            print(f"{dish}: ${price:.2f}")

# Customer class with order history
class Customer:
    def __init__(self, customer_name, phone_number):
        if Validations.is_valid_name(customer_name) and Validations.is_valid_phone_number(phone_number):
            self._customer_name = customer_name
            self._phone_number = phone_number
            self._order_history = []

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, new_customer_name):
        if Validations.is_valid_name(new_customer_name):
            self._customer_name = new_customer_name
        else:
            raise ValueError("Invalid customer name format")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, new_phone_number):
        if Validations.is_valid_phone_number(new_phone_number):
            self._phone_number = new_phone_number
        else:
            raise ValueError("Invalid phone number format")

    @property
    def order_history(self):
        return self._order_history

    @order_history.setter
    def order_history(self, new_order_history):
        if isinstance(new_order_history, list):
            self._order_history = new_order_history
        else:
            raise ValueError("Invalid order history format")

    def place_order(self, menu, selected_items):
        total_price = 0
        order_details = []

        for selected_item in selected_items:
            if selected_item in menu.menu_items:
                total_price += menu.menu_items[selected_item]
                order_details.append(selected_item)

        if order_details:
            order = {
                "items": order_details,
                "total_price": total_price
            }
            self._order_history.append(order)
            return f"Order placed. Total price: ${total_price:.2f}"
        else:
            return "No valid items selected for the order."

    def view_order_history(self):
        if not self._order_history:
            return "No order history available."
        else:
            print(f"Order history for {self.customer_name}:")
            for i, order in enumerate(self._order_history, start=1):
                print(f"Order {i}: {', '.join(order['items'])}, Total Price: ${order['total_price']:.2f}")


# Instantiate the menu items
appetizer1 = Appetizer("Spinach Dip", 8.99)
appetizer2 = Appetizer("Bruschetta", 6.99)
entree1 = Entree("Spaghetti Carbonara", 14.99)
entree2 = Entree("Chicken Alfredo", 16.99)

# Instantiate the restaurant menu
restaurant_menu = Restaurant_Menu()

# Add menu items to the restaurant menu
restaurant_menu.add_item(appetizer1)
restaurant_menu.add_item(appetizer2)
restaurant_menu.add_item(entree1)
restaurant_menu.add_item(entree2)

# Instantiate a customer
customer1 = Customer("John Doe", "5551234567")

# Place an order for the customer
order1 = customer1.place_order(restaurant_menu, ["Spinach Dip", "Chicken Alfredo"])

# View the order history for the customer
order_history = customer1.view_order_history()

# Output
print(f"Customer: {customer1.customer_name}, Phone Number: {customer1.phone_number}")
print(order1)
print(order_history)

# View the restaurant menu
restaurant_menu.view_menu()
