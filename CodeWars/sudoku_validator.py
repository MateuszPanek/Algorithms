from math import sqrt


class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.size = len(self.data)
        self.small_square = int(sqrt(self.size))
        self.mistakes = None
        self.result = bool
        self.slice = []

    def is_valid(self):
        pass

    def slice_check(self):
        pass

    # TODO - make sure that 0 is not seen as duplicate each time

    def check_squares(self):
        square_row = 0
        new_list = []
        # while square_row < self.size:
        square_start = 0
        row_start = 0
        row_stop = self.small_square
        square_stop = self.small_square
        square_count = 0
        # while square_row < self.size ** 2:
        for i in range(self.small_square):
            self.check_small_squares_even(row_start, row_stop)
            row_start += self.small_square
            row_stop += self.small_square
            square_start = 0
            square_stop = self.small_square
            print('___________')

            print('I changed parameters : row_start : {}\nrow_stop: {}\n'
                  'square_row is: {}'.format(row_start, row_stop, square_row))
            # while square_row < self.small_square:
            for i in range(self.small_square):
                itteration = 0
                print('New_list before clearing :', new_list)
                new_list.clear()
                print('New_list after clearing:', new_list)
                square_count += 1
                for part in self.slice:
                    print(part)

                    for item in part[square_start:square_stop]:
                        print('this is the part {}'.format(part[square_start:square_stop]))
                        new_list.append(item)
                        itteration += 1
                        print(itteration)
                        print(new_list)
                    if itteration == self.size:
                        itteration = 0
                        square_start += self.small_square
                        square_stop += self.small_square
                        print('I changed parameters to\nsquare_start: {}\nsquare_stop: {}'.format(square_start, square_stop))

                if len(new_list) != len(set(new_list)):
                    print(new_list)
                    checked = set()
                    duplicates = [x for x in new_list if x not in checked and not checked.add(x)]
                    print('Duplikaty : {} w kwadracie {}:'.format(duplicates, square_count))
                    print('Checked before cleaning:', checked)
                    checked.clear()
                    print('Checked after cleaning:', checked)
                    return False
                if sorted(new_list) != list(range(1, self.size + 1)):
                    print('Not all the integers were typed')
                    print(square_count)
                    return False

                print('at itteration :{} I reached this place'.format(itteration))

                # square_start += self.small_square
                # square_stop += self.small_square
                # new_list.clear()
                # square_count += 1
                print('Koniec kodu :',new_list)
                print('Square row : {}',format(square_row))
                # while square_start < self.size:
                #     if self.size % 2 != 0:
                #         self.check_small_squares_even(square_start, square_stop, square_row)
                #     else:
                #         self.check_small_squares_odds(square_start, square_stop, square_row)
                #
                #     print(len(self.mistakes))
                #     # if len(self.mistakes) > 0:
                #     #     return False
                #     square_start += self.small_square
                #     square_stop += self.small_square
                # square_row += self.small_square
        return True

    def check_small_squares_even(self, row_start, row_stop):
        # self.mistakes = [item for item in self.data[square_row][square_start:square_stop]
        #                  if item in self.data[square_row + 1][square_start:square_stop]
        #                  or item in self.data[square_row + 2][square_start:square_stop]]
        self.slice = self.data[row_start:row_stop]
        print(self.slice)
        # print(self.data[square_row][square_start:square_stop], '\n',
        #       self.data[square_row + 1][square_start:square_stop], '\n',
        #       self.data[square_row + 2][square_start:square_stop], '\n')

    def check_small_squares_odds(self, square_start, square_stop, square_row):
        self.mistakes = [item for item in self.data[square_row][square_start:square_stop]
                         if item in self.data[square_row + 1][square_start:square_stop]]

        print(self.data[square_row][square_start:square_stop], '\n',
              self.data[square_row + 1][square_start:square_stop], '\n')

    def check_rows(self):
        pass

    def check_columns(self):
        pass


# HOw to check - math sqrt (len(list[0)) = single square size,
# LEn (list) - gives me the N (to know what is the dimension of the square)
# len - 1 = index range for all sublists, and main list
# Validator = checks if single lists are unique,
# Checkes if all items in smaller squares - math.sqrt(len(list[0]) list[0], list[1], list[2],


goodSudoku1 = Sudoku([
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

goodSudoku2 = Sudoku([
    [1, 4, 2, 3],
    [3, 2, 4, 1],

    [4, 1, 3, 2],
    [2, 3, 1, 4]
])

badSudoku1 = Sudoku([
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

# goodSudoku1.check_squares()
# print(goodSudoku1.result)
# goodSudoku2.check_squares()
# print(goodSudoku2.result)

goodSudoku3 = Sudoku(
    [[0, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 3],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 3],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 2],

     [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 2],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1],

     [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 7, 7],

     [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 7, 7],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 7, 7],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 7, 7]])

# goodSudoku1.check_squares()
goodSudoku2.check_squares()
badSudoku1.check_squares()