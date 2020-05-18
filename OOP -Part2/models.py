class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

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


class Movie(Program):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


avengers = Movie('Avengers - Infinity War', 2018, 160)
atlanta = Series('atlanta', 2018, 2)

avengers.receive_likes()
avengers.receive_likes()
avengers.receive_likes()

atlanta.receive_likes()
atlanta.receive_likes()

print(f'Name: {avengers.name} - Likes: {avengers.likes}')
print(f'Name: {atlanta.name} - Likes: {atlanta.likes}')
