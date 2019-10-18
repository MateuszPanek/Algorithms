"""In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
You have function with one side of the DNA (string, except for Haskell); you need to
get the other complementary side. DNA strand is never empty or there is no DNA at all
(again, except for Haskell)."""


def DNA_strand(dna):
    complementary_side = {'A': 'T',
                          'C': 'G',
                          'G': 'C',
                          'T': 'A'
                          }

    return ''.join([complementary_side[letter] for letter in dna])


'''Interesting solution :'''


def DNA_strand1(dna):
    return dna.translate(dna.maketrans('ATCG', 'TAGC'))


