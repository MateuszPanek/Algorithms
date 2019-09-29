from random import randint
import pylab as pl
import numpy as np


class Dice(object):
    """Class that simulates dice throws and visualise throw statistics"""

    def __init__(self):
        self.numbers = []
        self.unique_numbers = {}

    def generate_number(self):
        return randint(1, 7)

    def generate_random_numbers(self, throws: int):
        self.numbers.clear()
        for i in range(throws):
            number = self.generate_number()
            self.numbers.append(number)
            self.count_unique_numbers(number)
        return self.numbers

    def count_unique_numbers(self, number):
        try:
            self.unique_numbers[number] += 1

        except KeyError:
            self.unique_numbers.setdefault(number, 1)

    def show_unique_numbers(self):
        return self.unique_numbers

    def show_statistics(self):
        X = np.arange(len(self.unique_numbers))
        pl.bar(X, self.unique_numbers.values(), align='center', width=0.5)
        pl.xticks(X, sorted(self.unique_numbers.keys()))
        ymax = int(max(self.unique_numbers.values()) * 1.2)
        pl.ylim(0, ymax)
        pl.show()


if __name__ == '__main__':
    game = Dice()
