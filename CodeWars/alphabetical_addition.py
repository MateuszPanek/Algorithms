
def alphabetical_addition(*letters):
    """Returns letter from alhabet which index is sum of all indexes of letters given as arguments"""
    import string
    alphabet = string.ascii_lowercase
    return alphabet[sum((letters.index(item) + 1) for item in letters) - 1 if len(letters) -1]