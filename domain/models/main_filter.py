from abc import ABC


class MainFilter(ABC):
    def __int__(self, date, text, number):
        self.date = date
        self.text = text
        self.number = number

