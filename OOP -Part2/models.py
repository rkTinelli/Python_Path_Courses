class Movie:
    def __init__(self, name, year, length):
        self.__name = name.title()
        self.year = year
        self.length = length
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def receive_likes(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def nome(self, name):
        self.__name = name


class Serie:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def receive_likes(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def nome(self, name):
        self.__name = name


avengers = Movie('Avengers - Infinity War', 2018, 160)
print(avengers.name)

atlanta = Serie('atlanta', 2018, 2)
print(f'Name: {atlanta.name} - Year: {atlanta.year}')
