def find_outlier(integers: list) -> int:
    """Function that returns 'outlier' N from the given array of integers that either consists of
    all odds integers either all even integers except of singe integer N"""
    evens = [i for i in integers if i % 2 == 0]
    odds = [i for i in integers if i % 2 != 0]
    return evens[0] if len(evens) < len(odds) else odds[0]


''' Most interesting solution found after solving KATA : '''


def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
