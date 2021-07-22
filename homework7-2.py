from abc import ABC, abstractmethod


классная Одежда:
    результат = 0

    def __init__(self, param):
        self.param = парам 

    @property
    @abstractmethod
    def cloth(self):
        проходить

    def __add__(self, other):
        Clothes.result += self.cloth + other.cloth
        возвратный костюм(0)

    def __str__(self):
        res = Одежда.
        Одежда.результат = 0
        return f"{res}"

классный костюм(Одежда):
    @property
    def cloth(self):
        обратный раунд((2 * self.param + 0.3) / 100)


классное пальто(Одежда):
    @property
    def cloth(self):
        обратный раунд(self.param / 6.5) + 0.5


пальто = Пальто(44)
масть = Масть(125)
принт(пальто + костюм)
