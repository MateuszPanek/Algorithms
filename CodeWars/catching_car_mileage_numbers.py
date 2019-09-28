def is_interesting(number, awesome_phrases):
    if number < 97:
        return 0
    for i in range(3):
        if number > 99:
            if i == 0:
                if str(number)[1:] == '0' * (len(str(number)) -1):
                    return 2
                if str(number) == str(number)[::-1]:
                    return 2
                if number in awesome_phrases:
                    return 2
                if str(number) in '1234567890' or str(number) in '0987654321':
                    return 2
                for i in range(len(str(number)) - 2):
                    if int(str(number)[i]) - 1 == int(str(number)[i + 1]):


            if i > 0:
                if str(number)[1:] == '0' * (len(str(number)) -1):
                    return 1
                if str(number) == str(number)[::-1]:
                    return 1
                if number in awesome_phrases:
                    return 1
                if number + 1 in awesome_phrases:
                    return 1
                if str(number) in '1234567890' or str(number) in '0987654321':
                    return 1
        number += 1



    return 0


print(is_interesting(11209, [1337, 256]))

""" Best pracice : """
def is_incrementing(number): return str(number) in '1234567890'


def is_decrementing(number): return str(number) in '9876543210'


def is_palindrome(number):   return str(number) == str(number)[::-1]


def is_round(number):        return set(str(number)[1:]) == set('0')


def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)

    for num, color in zip(range(number, number + 3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0
