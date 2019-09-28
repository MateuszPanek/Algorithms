def accum(s: str) -> str:
    """Function that returns given string - with each of it's elements multiplied by it's index + 1"""
    return '-'.join([(letter * (s.index(letter) + 1)).title() for letter in [item for item in s]])


def accum1(s: str) -> str:
    """Function that returns given string - with each of it's elements multiplied by it's index + 1"""
    return '-'.join([(s[i - 1] * i).title() for i in range(1, len(s) + 1)])


def find_it(seq: list) -> int:
    """Function that counts integers from a list and returns the one that is appearing even times"""
    count = {}
    for integer in seq:
        try:
            count[integer] += 1
        except KeyError:
            count.setdefault(integer, 1)

    for item in count:
        if count[item] % 2 != 0:
            return item

seq = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]


def find_it1(seq: list) -> int:
    """Function that counts integers from a list and returns the one that is appearing even times"""
    return [x for x in set(seq) if seq.count(x) % 2][0]

def get_middle(s: list):
    """Finds middle elements in a list"""
    middle = int(len(s) / 2)
    return s[middle - 1: middle + 1] if len(s) % 2 == 0 else s[middle]


def solution(number: list) -> int:
    """Sums up all integers that are divisible by 3 and 5 from given list"""
    return sum([item for item in range(1, number) if item % 3 == 0 or item % 5 == 0])

def high_and_low(numbers: str) -> str:
    """Returns a string consisting of max and min int from given string"""
    numbers = [int(item) for item in numbers.split(' ')]
    return ' '.join((str(max(numbers)), str(min(numbers))))

numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

def digital_root(n: int) -> int:
    """Breaks down given integer into sum of it's digits as long as integer will be one digit-long - recursion """
    root = sum([int(item) for item in str(n)])
    if len(str(root)) == 1:
        return root
    else:
        return digital_root(root)

def find_short(s: str) -> str:
    """Returns shortest of sub-strings in given string"""
    return min(len(item) for item in s.split(' '))

s = "bitcoin take over the world maybe who knows perhaps"

print(find_short(s))

def likes(names: list) -> str:
    """Return string with format based on number of given elements in a list"""
    try:
        if len(names) == 3:
            return '{}, {} and {} like this'.format(names[0], names[1], names[2])

        elif len(names) > 3:
            return '{}, {} and {} others like this'.format(names[0], names[1], len(names) - 2)

        elif len(names) == 2:
            return '{} like this'.format(' and '.join(names))

        else:
            return f'{names[0]} likes this'

    except IndexError:
        return 'no one like this'

def likes2(names):
    """Return string with format based on number of given elements in a list"""
    amount_of_names = len(names)
    options = {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }

    return options[min(4, amount_of_names)].format(*names, others=amount_of_names - 2)

def camel_case(string: str) -> str:
    """Returns CamelCase version of given string"""
    return string.title().replace(' ', '')

def row_sum_odd_numbers(n):
    triangle = []
    """Returns sum of odd numbers in specified triangle row index
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
"""
    start, stop, row = 1, 2, 1
    while row <= n:
        triangle.append(list(range(start, stop, 2)))
        start = triangle[row - 1][-1] + 2
        row += 1
        stop += 2 * row

    return sum(triangle[n - 1])


"""best practice : sum of ints in a row equals to row index ** 3 """

def row_sum_odd_numbers1(n):
    return n**3

