
from sudoku_validator import SudokuValidator

class SudokuGameEngine(object):

    def __init__(self, size:int):
        self.size = 9 if None else size
        self.board = [[0 for i in range(size)] for i in range(size)]
        self.validate = SudokuValidator(self.board)

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print('- - - - - - - - - - - -')

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(' | ', end='')

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + ' ', end='')


    def input_a_number(self):
        i = list(input('Select row and position of your input and provide with a number'))
        self.board[int(i[0])][int(i[1])] = int(i[2])

    def game(self):
        while True:
            self.print_board()
            self.input_a_number()
            self.ready_to_valid()

    def ready_to_valid(self):
        if 0 not in self.board:
            decision = input('Are you ready to finish Y/N?')
            if decision == 'Y':
                self.validate.is_valid()
                if self.validate.evaluate == True:
                    print('Congrats, you have won!')
                if self.validate.evaluate == False:
                    print('Better luck next time!')

if __name__ == '__main__':

    size = int(input('What size of board would you like?'))
    Game = SudokuGameEngine(size)
    Game.game()

