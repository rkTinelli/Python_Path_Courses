class Show:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    def __str__(self):
        return f'Name: {self._name} - Likes: {self._likes}'

    @property
    def likes(self):
        return self._likes

    def receive_likes(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def nome(self, name):
        self._name = name


class Movie(Show):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    def __str__(self):
        return f'Name: {self._name} - {self.length} min - Likes: {self._likes}'


class Series(Show):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Name: {self._name} - {self.seasons} seasons - Likes: {self._likes}'


class Playlist():
    def __init__(self, name, shows):
        self.nome = name
        self._shows = shows

    def __getitem__(self, item):
        return self._shows[item]

    def __len__(self):
        return len(self._shows)


avengers = Movie('Avengers Infinity War', 2018, 160)
john_wick = Movie('John Wick', 2014, 107)
atlanta = Series('atlanta', 2018, 2)
b99 = Series('Brooklyn Nine-Nine ', 2013, 7)

avengers.receive_likes()
avengers.receive_likes()
avengers.receive_likes()

john_wick.receive_likes()
john_wick.receive_likes()

atlanta.receive_likes()
atlanta.receive_likes()

b99.receive_likes()
b99.receive_likes()
b99.receive_likes()
b99.receive_likes()

playlist = [avengers,atlanta, john_wick, b99]

print(f'Playlist size: {len(playlist)} items')

for show in playlist:
    print(show)