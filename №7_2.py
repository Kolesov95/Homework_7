from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return round((self.size / 6.5 + 0.5), 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        return self.height * 2 + 0.3


a = Coat(41)
print(a.consumption)
b = Suit(40)
print(b.consumption)
