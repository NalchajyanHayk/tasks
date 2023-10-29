from validations import Validations
from abc import ABC, abstractmethod
from validations import Validations


class Movie:
    def __init__(self, title, genre, length):
        self._title = None
        self._genre = None
        self._length = None

        self.title = title
        self.genre = genre
        self.length = length

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if Validations.is_valid_name(value):
            self._title = value
        else:
            print("Invalid movie title format.")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if Validations.game_genres(value):
            self._genre = value
        else:
            print("Invalid movie genre format.")

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if Validations.is_positive_number(value):
            self._length = value
        else:
            print("Invalid movie length.")

class Theater(ABC):
    def __init__(self, location, seating_capacity):
        self._location = None
        self._seating_capacity = None

        self.location = location
        self.seating_capacity = seating_capacity

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if Validations.is_valid_address(value):
            self._location = value
        else:
            print("Invalid location format.")

    @property
    def seating_capacity(self):
        return self._seating_capacity

    @seating_capacity.setter
    def seating_capacity(self, value):
        if Validations.is_positive_number(value):
            self._seating_capacity = value
        else:
            print("Invalid seating capacity.")

    @abstractmethod
    def display_info(self):
        pass

class StandardTheater(Theater):
    def display_info(self):
        print(f"Location: {self.location}, Seating Capacity: {self.seating_capacity}, Type: Standard")

class IMAXTheater(Theater):
    def display_info(self):
        print(f"Location: {self.location}, Seating Capacity: {self.seating_capacity}, Type: IMAX")

class Showtime:
    def __init__(self, movie, theater, showtime):
        self._movie = None
        self._theater = None
        self._showtime = None

        self.movie = movie
        self.theater = theater
        self.showtime = showtime

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, value):
        if isinstance(value, Movie):
            self._movie = value
        else:
            print("Invalid movie format.")

    @property
    def theater(self):
        return self._theater

    @theater.setter
    def theater(self, value):
        if isinstance(value, Theater):
            self._theater = value
        else:
            print("Invalid theater format.")

    @property
    def showtime(self):
        return self._showtime

    @showtime.setter
    def showtime(self, value):
        if Validations.is_valid_date(value):
            self._showtime = value
        else:
            print("Invalid showtime format.")

movie1 = Movie("Movie 1", "Action", 120)
standard_theater = StandardTheater("Location 1", 100)
imax_theater = IMAXTheater("Location 2", 50)

showtime1 = Showtime(movie1, standard_theater, "2023-11-01 18:00")
showtime2 = Showtime(movie1, imax_theater, "2023-11-01 20:00")

for showtime in [showtime1, showtime2]:
    print(f"Movie: {showtime.movie.title}, Genre: {showtime.movie.genre}, Length: {showtime.movie.length} minutes")
    showtime.theater.display_info()
    print(f"Showtime: {showtime.showtime}")
    print()

