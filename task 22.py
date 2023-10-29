from abc import ABC, abstractmethod
from validations import Validations

class GamingOperations(ABC):
    @abstractmethod
    def play_game(self, player):
        pass

    @abstractmethod
    def save_game_progress(self, player, game, progress):
        pass

    @abstractmethod
    def compete(self, player1, player2, game):
        pass

class Game:
    def __init__(self, title, genre, release_date):
        self.__title = None
        self.__genre = None
        self.__release_date = None

        self.title = title
        self.genre = genre
        self.release_date = release_date

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if Validations.is_valid_name(value):
            self.__title = value
        else:
            print("Invalid title format.")

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if Validations.game_genres(value):
            self.__genre = value
        else:
            print("Invalid genre format.")

    @property
    def release_date(self):
        return self.__release_date

    @release_date.setter
    def release_date(self, value):
        if Validations.is_valid_date(value):
            self.__release_date = value
        else:
            print("Invalid date format.")

class Player:
    def __init__(self, name, contact_info):
        self.__name = None
        self.__contact_info = None

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

class Console:
    def __init__(self, console_type):
        self.__console_type = None
        self.__games_installed = []

        self.console_type = console_type

    @property
    def console_type(self):
        return self.__console_type

    @console_type.setter
    def console_type(self, value):
        if Validations.is_valid_name(value):
            self.__console_type = value
        else:
            print("Invalid console type format.")

    @property
    def games_installed(self):
        return self.__games_installed

    def install_game(self, game):
        if isinstance(game, Game) and game not in self.__games_installed:
            self.__games_installed.append(game)
            print(f"{game.title} has been installed on {self.__console_type} console.")
        else:
            print("Invalid game or game already installed.")

    def uninstall_game(self, game):
        if game in self.__games_installed:
            self.__games_installed.remove(game)
            print(f"{game.title} has been uninstalled from {self.__console_type} console.")
        else:
            print("Game not installed on this console.")

class SportsGame(Game):
    def __init__(self, title, release_date):
        super().__init__(title, "Sports", release_date)

class AdventureGame(Game):
    def __init__(self, title, release_date):
        super().__init__(title, "Adventure", release_date)

# Example usage:

game1 = SportsGame("FIFA 2023", "2023-09-15")
game2 = AdventureGame("The Legend of Zelda: Breath of the Wild", "2017-03-03")

player1 = Player("Player 1", "player1@example.com")
player2 = Player("Player 2", "player2@example.com")

console1 = Console("Xbox Series X")
console2 = Console("PlayStation 5")

console1.install_game(game1)
console2.install_game(game2)

console1.uninstall_game(game2)
console2.install_game(game1)

console1.games_installed

console2.games_installed
