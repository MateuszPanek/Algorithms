""""
You are now to create a function that returns a Josephus permutation, taking as parameters
the initial array/list of items to be permuted as if they were in a circle and counted out
every k places until none remained.
"""

def josephus(items, k):
    sequence = []
    iteration = 0
    while len(items) > 0:
        index = 0
        for i in range(len(items)):
            iteration += 1
            if iteration % k == 0:
                sequence.append(items.pop(index))
                continue
            index += 1

    return sequence

items, k = list(range(1, 11)), 1
items2, k2 = list(range(1, 8)), 3
result = josephus(items, k)

assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'Not a Josephus style!'

result2 = josephus(items2, k2)

assert result2 == [3, 6, 2, 7, 5, 1, 4], 'Not a Josephus style!'
