from math import sqrt


class SudokuValidator(object):
    def __init__(self, data):
        self.data = data
        self.size = len(self.data)
        self.small_square = int(sqrt(self.size))
        self.slice = []
        self.evaluate = True

    def is_valid(self):
        self.size_check()
        self.rows_check()
        self.columns_check()
        self.check_all_squares()
        return self.evaluate

    def columns_check(self):
        for itteration in range(self.size):
            checked_column = []
            for column in self.data:
                checked_column.append(column[itteration])
            self.check_if_all_integers_were_typed(checked_column)
            self.find_duplicates(checked_column, itteration)
        return self.evaluate

    def rows_check(self):
        row_count = 0
        for row in self.data:
            row_count += 1
            self.find_duplicates(row, row_count)
            self.check_if_all_integers_were_typed(row)
        return self.evaluate
    # TODO - make sure that 0 is not seen as duplicate each time

    def check_all_squares(self):
        row_start = 0
        row_stop = self.small_square
        square_count = 0
        for i in range(self.small_square):
            self.slice_the_square(row_start, row_stop)
            row_start += self.small_square
            row_stop += self.small_square
            square_start = 0
            square_stop = self.small_square
            for i in range(self.small_square):
                itteration = 0
                new_list = []
                square_count += 1
                for part in self.slice:
                    for item in part[square_start:square_stop]:
                        new_list.append(item)
                        itteration += 1
                    if itteration == self.size:
                        itteration = 0
                        square_start += self.small_square
                        square_stop += self.small_square
                self.find_duplicates(new_list, square_count)
                self.check_if_all_integers_were_typed(new_list)
        return self.evaluate

    def size_check(self):
        for row in self.data:
            if len(row) != len(self.data):
                self.evaluate = False

    def slice_the_square(self, row_start, row_stop):
        self.slice = self.data[row_start:row_stop]

    def check_if_all_integers_were_typed(self, list_of_integers):
        if sorted(list_of_integers) != list(range(1, self.size + 1)):
            print('Not all the integers were typed')
            self.evaluate = False

    def find_duplicates(self, list_of_integers, counter):
        if len(list_of_integers) != len(set(list_of_integers)):
            checked = set()
            duplicates = [x for x in list_of_integers if x not in checked and not checked.add(x)]
            print('Duplicates : {} in square/row/column {}:'.format(duplicates, counter))
            self.evaluate = False





goodSudoku1 = SudokuValidator([
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],

    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],

    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4]
])

goodSudoku2 = SudokuValidator([
    [1, 4, 2, 3],
    [3, 2, 4, 1],

    [4, 1, 3, 2],
    [2, 3, 1, 4]
])

badSudoku1 = SudokuValidator([
    [0, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
])
