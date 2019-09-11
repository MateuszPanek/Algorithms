"""
Task

Given an array/list [] of n integers , Arrange them in a way similar to the to-and-fro movement of a Pendulum

The Smallest element of the list of integers , must come in center position of array/list.

The Higher than smallest , goes to the right .
The Next higher number goes to the left of minimum number and So on , in a to-and-fro manner similar to that
of a Pendulum.

"""

"""
Solution below was too slow to pass

def pendulum(values):
    values = sorted(values)
    new_values = []
    for n in range(- 1, len(values) - 1, 2):
        try:
            new_values.insert(0, values[n + 1])
            new_values.append(values[n + 2])
        except IndexError:
            pass

    return new_values
"""


def pendulum(values):
    values = sorted(values)
    if len(values) % 2 == 0:
        return values[len(values)-2:1:-2] + [values[0]] + values[1::2]
    else:
        return values[len(values):1:-2] + [values[0]] + values[1::2]


values = [4,6,8,7,5]
values2 = [19,30,16,19,28,26,28,17,21,17]


outcome = [8,6,4,5,7]
outcome2 = [28,26,19,17,16,17,19,21,28,30]

print("Expected outcome: {}".format(outcome))
result = pendulum(values)
print("Your outcome: {}".format(result))

print("Expected outcome: {}".format(outcome2))
result2 = pendulum(values2)
print("Your outcome: {}".format(result2))


assert result == [8,6,4,5,7], "Wrong outcome!"
assert result2 == [28,26,19,17,16,17,19,21,28,30], "Wrong outcome!"

"""

SIMPLEST SOLUTION

def pendulum1(a):
    a = sorted(a)
    return a[::2][::-1] + a[1::2]

a = sorted(values)

print(a[::2][::-1] + a[1::2])

"""