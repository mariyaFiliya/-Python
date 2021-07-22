from abc import ABC, abstractmethod


class Clothes:
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def cloth(self):
        pass

    def __add__(self, other):
        Clothes.result += self.cloth + other.cloth
        return Suit(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"

class Suit(Clothes):
    @property
    def cloth(self):
        return round((2 * self.param + 0.3) / 100)


class Coat(Clothes):
    @property
    def cloth(self):
        return round(self.param / 6.5) + 0.5


coat = Coat(44)
suit = Suit(125)
print(coat + suit)
