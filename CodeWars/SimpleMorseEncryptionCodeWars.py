"""
Write a function that will encrypt a given sentence into International Morse Code, both the input and out puts will be strings.

Characters should be separated by a single space. Words should be separated by a triple space.

For example, "HELLO WORLD" should return -> ".... . .-.. .-.. --- .-- --- .-. .-.. -.."

To find out more about Morse Code follow this link: https://en.wikipedia.org/wiki/Morse_code

A preloaded object/dictionary/hash called CHAR_TO_MORSE will be provided to help convert characters to Morse Code.
"""

CHAR_TO_MORSE = {'0': '-----', '2': '..---', '4': '....-', '6': '-....', '8': '---..',
                 'B': '-...', 'D': '-..', 'F': '..-.', 'H': '....', 'J': '.---',
                 'L': '.-..', 'N': '-.', 'P': '.--.', 'R': '.-.', 'T': '-', 'V': '...-',
                 'X': '-..-', 'Z': '--..', 'b': '-...', 'd': '-..', 'f': '..-.',
                 'h': '....', 'j': '.---', 'l': '.-..', 'n': '-.', 'p': '.--.', 'r': '.-.',
                 't': '-', 'v': '...-', 'x': '-..-', 'z': '--..', '1': '.----', '3': '...--',
                 '5': '.....', '7': '--...', '9': '----.', 'A': '.-', 'C': '-.-.', 'E': '.',
                 'G': '--.', 'I': '..', 'K': '-.-', 'M': '--', 'O': '---', 'Q': '--.-', 'S': '...',
                 'U': '..-', 'W': '.--', 'Y': '-.--', 'a': '.-', 'c': '-.-.', 'e': '.', 'g': '--.',
                 'i': '..', 'k': '-.-', 'm': '--', 'o': '---', 'q': '--.-', 's': '...', 'u': '..-',
                 'w': '.--', 'y': '-.--'}

# Two approaches - first one is not requiring us to modify given dictionary, second makes it simpler by simple modification

def encryption(string):
    word = []
    for item in list(string):
        try:
            word.append(CHAR_TO_MORSE[item])
        except KeyError:
            word.append(' ')

    return ' '.join(word)

def encryption1(string):
    CHAR_TO_MORSE[' '] = ' '
    return ' '.join([CHAR_TO_MORSE[item] for item in list(string)])

input_message = 'HELLO WORLD'
expected_outcome = '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'

print('Your expected outcome is {}'.format(expected_outcome))
result = encryption1(input_message)
print('Your outcome is {}'.format(encryption(input_message)))

assert result == '.... . .-.. .-.. ---   .-- --- .-. .-.. -..', 'Your encryption is not correct'

