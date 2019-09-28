"""Solution for KATA calculating with functions"""

def zero(calc=None):
    return calc(0) if calc else 0


def one(calc=None):
    return calc(1) if calc else 1


def two(calc=None):
    return calc(2) if calc else 2


def three(calc=None):
    return calc(3) if calc else 3


def four(calc=None):
    return calc(4) if calc else 4


def five(calc=None):
    return calc(5) if calc else 5


def six(calc=None):
    return calc(6) if calc else 6


def seven(calc=None):
    return calc(7) if calc else 7


def eight(calc=None):
    return calc(8) if calc else 8


def nine(calc=None):
    return calc(9) if calc else 9


def plus(n):
    return lambda x: x + n


def minus(n):
    return lambda x: x - n


def times(n):
    return lambda x: x * n


def divided_by(n):
    return lambda x: x // n


print(two(plus(five())))
