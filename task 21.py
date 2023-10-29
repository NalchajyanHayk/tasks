from validations import  Validations

class Song:
    def __init__(self, title, artist, duration):
        self._title = None
        self._artist = None
        self._duration = None
        self.title = title
        self.artist = artist
        self.duration = duration

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if Validations.is_valid_name(value):
            self._title = value
        else:
            print("Invalid title format.")

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, value):
        if Validations.is_valid_name(value):
            self._artist = value
        else:
            print("Invalid artist format.")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if Validations.is_positive_number(value):
            self._duration = value
        else:
            print("Invalid duration format.")

class Artist:
    def __init__(self, name, contact_info):
        self._name = None
        self._contact_info = None
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

class User:
    def __init__(self, name, contact_info):
        self._name = None
        self._contact_info = None
        self._favorite_songs = []
        self._favorite_artists = []
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
    def favorite_songs(self):
        return self._favorite_songs

    @property
    def favorite_artists(self):
        return self._favorite_artists

    def add_favorite_song(self, song):
        if song not in self._favorite_songs:
            self._favorite_songs.append(song)

    def add_favorite_artist(self, artist):
        if artist not in self._favorite_artists:
            self._favorite_artists.append(artist)

# Instantiate objects

song1 = Song("Song 1", "Artist 1", 3.5)
song2 = Song("Song 2", "Artist 2", 4.2)
song3 = Song("Song 3", "Artist 3", 2.8)

artist1 = Artist("Artist 1", "artist1@example.com")
artist2 = Artist("Artist 2", "artist2@example.com")
artist3 = Artist("Artist 3", "artist3@example.com")

user1 = User("User 1", "user1@example.com")
user2 = User("User 2", "user2@example.com")

# Add songs and artists to the user's favorites

user1.add_favorite_song(song1)
user1.add_favorite_song(song2)
user1.add_favorite_artist(artist1)
user1.add_favorite_artist(artist2)

user2.add_favorite_song(song2)
user2.add_favorite_song(song3)
user2.add_favorite_artist(artist2)
user2.add_favorite_artist(artist3)
