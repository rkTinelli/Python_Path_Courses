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


avengers = Movie('Avengers Infinity War', 2018, 160)
atlanta = Series('atlanta', 2018, 2)

avengers.receive_likes()
avengers.receive_likes()
avengers.receive_likes()

atlanta.receive_likes()
atlanta.receive_likes()

playlist = [avengers,atlanta]

for show in playlist:
    print(show)