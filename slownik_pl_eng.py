class Translate(object):
    """Simple Polish-English dictionary with sentence translation option"""

    # TODO: finalise app logic - notification when deleting items
    def __init__(self, dict_pl=None):
        if type(dict_pl) != 'dict' and dict_pl is not None:
            raise SystemExit('Jesteś w 7 procentach...')
        self.dict_pl = {} if dict_pl is None else dict_pl

    def add_pair(self, pl, eng):
        if pl not in self.dict_pl.keys():
            self.dict_pl[pl] = eng
        else:
            return 'Słowo już jest w słowniku, użyj funkcji update'

    def get_translation(self, pl):
        try:
            return self.dict_pl[pl]

        except KeyError:
            return 'Nie znalazłem słowa!'

    def update_pair(self, pl, eng):
        ans = input('Czy na pewno chcesz edytować? T/N')
        if ans == 'T':
            self.add_pair(pl, eng)
        return False

    def remove_pair(self, pl):
        del self.dict_pl[pl]

    def translate_sentence_pl_to_eng(self, *sentence):
        try:
            return ' '.join([self.dict_pl[item] for item in sentence])
        except KeyError:
            print('Jedno ze słów nie zostało zdefiniowane')

    def quit_slownik(self):
        ans = input('Czy chcesz zapisać zmiany? T/N')
        if ans == 'T':
            self.save_file()
        else:
            exit(0)

    def save_file(self):
        with open('dict.txt', 'w') as dict_text:
            for k, v in self.dict_pl.items():
                print(k, ':', v, file=dict_text)

    def open_file(self):
        with open('dict.txt', 'r') as dict_text:
            for line in dict_text:
                self.dict_pl[(line.split()[0])] = line.split()[2]


if __name__ == '__main__':
    slownik = Translate()
    try:
        slownik.open_file()
    except FileNotFoundError:
        print('Brak pliku do wczytania')
