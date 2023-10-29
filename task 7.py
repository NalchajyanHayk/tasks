from abc import ABC, abstractmethod

class Movie(ABC):
    def __init__(self, title, genre, rating):
        if not self._is_valid_title(title):
            raise ValueError("Invalid title format")
        if not self._is_valid_genre(genre):
            raise ValueError("Invalid genre format")
        if not self._is_valid_rating(rating):
            raise ValueError("Invalid rating format")
        self._title = title
        self._genre = genre
        self._rating = rating

    @abstractmethod
    def display_info(self):
        pass

    @property
    def title(self):
        return self._title

    @property
    def genre(self):
        return self._genre

    @property
    def rating(self):
        return self._rating

    def _is_valid_title(self, title):
        # Validation logic for title
        return isinstance(title, str) and title

    def _is_valid_genre(self, genre):
        # Validation logic for genre
        return isinstance(genre, str) and genre

    def _is_valid_rating(self, rating):
        # Validation logic for rating
        return isinstance(rating, str) and rating

class ComedyMovie(Movie):
    def display_info(self):
        return f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}, Type: Comedy"

class DramaMovie(Movie):
    def display_info(self):
        return f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}, Type: Drama"

class Customer:
    def __init__(self, name, contact_info):
        if not self._is_valid_name(name):
            raise ValueError("Invalid name format")
        if not self._is_valid_contact_info(contact_info):
            raise ValueError("Invalid contact info format")
        self._name = name
        self._contact_info = contact_info
        self._rental_history = []

    @property
    def name(self):
        return self._name

    @property
    def contact_info(self):
        return self._contact_info

    def rent_movie(self, movie, rental_duration):
        rental = Rental(self, movie, rental_duration)
        self._rental_history.append(rental)
        return rental

    def view_rental_history(self):
        return self._rental_history

    def _is_valid_name(self, name):
        # Validation logic for name
        return isinstance(name, str) and name

    def _is_valid_contact_info(self, contact_info):
        # Validation logic for contact_info
        return isinstance(contact_info, str) and contact_info

class Rental:
    def __init__(self, customer, movie, rental_duration):
        if not self._is_valid_rental_duration(rental_duration):
            raise ValueError("Invalid rental duration format")
        self._customer = customer
        self._movie = movie
        self._rental_duration = rental_duration
        self._returned = False

    @property
    def customer(self):
        return self._customer

    @property
    def movie(self):
        return self._movie

    @property
    def rental_duration(self):
        return self._rental_duration

    @property
    def returned(self):
        return self._returned

    def return_rental(self):
        if not self._returned:
            self._returned = True
            return "Rental successfully returned."
        else:
            return "Rental already returned."

    def _is_valid_rental_duration(self, rental_duration):
        # Validation logic for rental_duration
        return isinstance(rental_duration, int) and rental_duration > 0

# Instantiate movies
comedy_movie = ComedyMovie("The Big Lebowski", "Comedy", "PG-13")
drama_movie = DramaMovie("The Shawshank Redemption", "Drama", "R")

# Instantiate a customer
customer = Customer("John Doe", "john@example.com")

# Rent movies
rental1 = customer.rent_movie(comedy_movie, 3)
rental2 = customer.rent_movie(drama_movie, 7)

# Return a rental
return_status = rental1.return_rental()

# View rental history
rental_history = customer.view_rental_history()

# Display movie information and rental history
for movie in [comedy_movie, drama_movie]:
    print(movie.display_info())

print("\nCustomer Rental History:")
for rental in rental_history:
    print(f"{rental.movie.title} ({rental.rental_duration} days) - Returned: {rental.returned}")

print("\nReturn Status:", return_status)
