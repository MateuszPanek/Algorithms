from numpy import prod


def persistence(n: int) -> int:
    """Function persistence, that takes in a positive parameter
    num and returns its multiplicative persistence, which is the number
    of times you must multiply the digits in num until you reach a single digit."""
    i = 0
    while True:
        if n < 10:
            return i
        n = prod([int(item) for item in str(n)])
        i += 1
