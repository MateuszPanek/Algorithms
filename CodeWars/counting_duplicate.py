def duplicate_count(array: str) -> int:
    """Returns number of duplicated characters found in given string"""
    return sum([1 for letter in set(array) if array.count(letter) > 1])

