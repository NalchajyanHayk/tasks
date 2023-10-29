from abc import ABC, abstractmethod

class RealEstateOperation(ABC):
    @abstractmethod
    def list_property(self, property):
        pass

    @abstractmethod
    def remove_property(self, property):
        pass

    @abstractmethod
    def add_client(self, client):
        pass

    @abstractmethod
    def remove_client(self, client):
        pass

    @abstractmethod
    def search_properties(self, client, search_criteria):
        pass

# Interface for different types of properties
class Property(ABC):
    def __init__(self, address, price, features):
        self.address = address
        self.price = price
        self.features = features

    @abstractmethod
    def property_type(self):
        pass

class Residential(Property):
    def property_type(self):
        return "Residential"

class Commercial(Property):
    def property_type(self):
        return "Commercial"

class Agent(RealEstateOperation):
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.property_listings = []
        self.clients = []

    def list_property(self, property):
        self.property_listings.append(property)

    def remove_property(self, property):
        if property in self.property_listings:
            self.property_listings.remove(property)

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self, client):
        if client in self.clients:
            self.clients.remove(client)

    def search_properties(self, client, search_criteria):
        matching_properties = []
        for property in self.property_listings:
            if all(keyword in property.features for keyword in search_criteria):
                matching_properties.append(property)
        return matching_properties

class Client(RealEstateOperation):
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.properties_purchased = []

    def list_property(self, property):
        raise NotImplementedError("Clients cannot list properties.")

    def remove_property(self, property):
        raise NotImplementedError("Clients cannot remove properties.")

    def add_client(self, client):
        raise NotImplementedError("Clients cannot add other clients.")

    def remove_client(self, client):
        raise NotImplementedError("Clients cannot remove other clients.")

    def search_properties(self, client, search_criteria):
        raise NotImplementedError("Clients cannot search for properties.")

    def purchase_property(self, property):
        self.properties_purchased.append(property)

# Example usage
if __name__ == "__main__":
    residential_property = Residential("123 Main St", 250000, ["3 bedrooms", "2 bathrooms"])
    commercial_property = Commercial("456 Oak Ave", 500000, ["Office space", "Parking"])

    agent1 = Agent("John Doe", "john@example.com")
    client1 = Client("Alice Smith", "alice@example.com")

    agent1.list_property(residential_property)
    agent1.list_property(commercial_property)
    agent1.add_client(client1)

    search_criteria = ["3 bedrooms"]
    matches = agent1.search_properties(client1, search_criteria)
    for property in matches:
        print(f"Matching {property.property_type()} property: {property.address}")

    client1.purchase_property(residential_property)
    print(f"{client1.name} purchased {residential_property.address}")
