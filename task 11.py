from abc import ABC, abstractmethod
from datetime import datetime
from validations import Validations

class Game_Operation(ABC):
    @abstractmethod
    def create_game(self, game):
        pass

    @abstractmethod
    def manage_game(self, game):
        pass


class Game(ABC):
    def __init__(self, title, genre, release_date):
        self._title = title
        self._genre = genre
        self._release_date = release_date

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and title:
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str) and genre:
            self._genre = genre
        else:
            raise ValueError("Genre must be a non-empty string")

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        if isinstance(release_date, datetime):
            self._release_date = release_date
        else:
            raise ValueError("Invalid release date")

    @abstractmethod
    def game_type(self):
        pass

class Action_Game(Game):
    def game_type(self):
        return "Action"

class Strategy_Game(Game):
    def game_type(self):
        return "Strategy"

class Developer(Game_Operation):
    def __init__(self, name, contact_info):
        self._name = None
        self._contact_info = None
        self._games = []

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
    def games(self):
        return self._games

    def create_game(self, game):
        if isinstance(game, Game):
            self._games.append(game)
        else:
            raise ValueError("Invalid game object")

    def manage_game(self, game):
        if game in self._games:
            self._games.remove(game)

from validations import Validations
class Publisher(Game_Operation):
    def __init__(self, name, contact_info):
        self._name = None
        self._contact_info = None
        self._released_games = []

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
    def released_games(self):
        return self._released_games

    def create_game(self, game):
        if isinstance(game, Game):
            self._released_games.append(game)
        else:
            raise ValueError("Invalid game object")

    def manage_game(self, game):
        if game in self._released_games:
            self._released_games.remove(game)

# Example usage
if __name__ == "__main__":
    action_game = Action_Game("Game of War", "Action", datetime(2023, 1, 15))
    strategy_game = Strategy_Game("Empire Builder", "Strategy", datetime(2023, 3, 10))

    developer1 = Developer("GameDev Inc.", "dev@example.com")
    publisher1 = Publisher("GamePub Ltd.", "pub@example.com")

    developer1.create_game(action_game)
    developer1.create_game(strategy_game)

    publisher1.create_game(action_game)
    publisher1.create_game(strategy_game)

    developer1.manage_game(action_game)

    print(f"{developer1.name} has developed the following games:")
    for game in developer1.games:
        print(f"{game.title} ({game.game_type()}), Released on {game.release_date}")

    print(f"{publisher1.name} has published the following games:")
    for game in publisher1.released_games:
        print(f"{game.title} ({game.game_type()}), Released on {game.release_date}")

