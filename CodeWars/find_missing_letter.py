import string

def find_missing_letter(chars):
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)

    try:
        return ''.join([letter for letter in alphabet_lower[alphabet_lower.index(sorted(chars)[0]):
                alphabet_lower.index(sorted(chars)[-1]) + 1] if letter not in chars])
    except ValueError:
        return ''.join([letter for letter in alphabet_upper[alphabet_upper.index(sorted(chars)[0]):
                alphabet_upper.index(sorted(chars)[-1]) + 1] if letter not in chars])



