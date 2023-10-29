from abc import ABC, abstractmethod
from datetime import datetime
from validations import Validations

# Validation class for input validation


# Abstract class for music
class Music(ABC):
    def __init__(self, title, artist):
        self._title = title
        self._artist = artist

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            self._title = new_title
        else:
            raise ValueError("Title must be a string")

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, new_artist):
        if isinstance(new_artist, str):
            self._artist = new_artist
        else:
            raise ValueError("Artist must be a string")

# Class for songs
class Song(Music):
    def __init__(self, title, artist, length):
        super().__init__(title, artist)
        if Validations.is_positive_number(length):
            self._length = length
        else:
            raise ValueError("Length must be a positive number")

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_length):
        if Validations.is_positive_number(new_length):
            self._length = new_length
        else:
            raise ValueError("Length must be a positive number")

# Abstract class for albums
class Album(Music):
    def __init__(self, title, artist, release_date):
        super().__init__(title, artist)
        self._release_date = release_date

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, new_release_date):
        if isinstance(new_release_date, datetime):
            self._release_date = new_release_date
        else:
            raise ValueError("Release date must be a datetime object")

class Playlist:
    def __init__(self, name):
        self._name = name
        self._songs = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Name must be a string")

    def add_song(self, song):
        if isinstance(song, Song):
            self._songs.append(song)
        else:
            raise ValueError("You can only add songs to the playlist")

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)
        else:
            raise ValueError("Song not found in the playlist")

    def view_playlist(self):
        print(f"Playlist: {self._name}")
        for i, song in enumerate(self._songs, start=1):
            print(f"{i}. {song.title} - {song.artist}")

# Example usage
song1 = Song("Song 1", "Eminem", 3.5)
song2 = Song("Song 2", "50 cent", 4.2)
album1 = Album("Album 1", "Artist 1", datetime(2022, 1, 1))
playlist1 = Playlist("My Playlist")

playlist1.add_song(song1)
playlist1.add_song(song2)

playlist1.view_playlist()
