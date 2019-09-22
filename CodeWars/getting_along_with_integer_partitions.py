"""
Codewars Kata Solution : Getting along with Integer Partitions

"""
import numpy as np


def partitions(n, I=1):
    yield (n,)
    for i in range(I, n // 2 + 1):
        for p in partitions(n - i, i):
            yield (i,) + p


def part(n):
    calculation_list = []
    for item in list(partitions(n)):
        calculation_list.append(np.product(item))
    calculation_list = sorted(set(calculation_list))
    average = sum(calculation_list) / len(calculation_list)
    range = calculation_list[-1] - calculation_list[0]
    if len(calculation_list) % 2 == 0:
        middle = int(len(calculation_list) / 2)
        median = ((calculation_list[middle - 1]) + int(calculation_list[middle])) / 2
    else:
        median = float(calculation_list[int(len(calculation_list) / 2 - 0.5)])

    return 'Range: {} Average: {:.2f} Median: {:.2f}'.format(range, average, median)


"""

Compatilbility with python 2 requires division by 2.0 instead of 2 and conversion of len(calculation_list)
to float

Useful functions found in different solutions in numpy module : median
from numpy import median, mean, prod


"""
