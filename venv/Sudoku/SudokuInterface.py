from tkinter import *
from sudoku_game_engine import *
from sudoku_validator import SudokuValidator


class SudokuInterface(object):

    def __init__(self, size=9):
        self.game = SudokuGameEngine(size)
        self.window = Tk()
        self.top_frame = Frame(self.window, width=800, height=400)
        self.bottom_frame = Frame(self.window, width=800, height=400)
        self.list_of_buttons = []
        self.entry = Entry(self.top_frame, width=2)
        self.num = 1
        self.gameboard = [[0 for j in range(9)] for i in range(9)]
        self.gameboard1 = [[0 for j in range(9)] for i in range(9)]
    def game_interface(self):
        self.window.title = ('Sudoku v 1.0')
        # self.window.geometry =('900x900')
        self.frames_init()
        # self.entry_box()
        self.board_creation()
        self.submit_button()
        self.clear_button()
        self.label_init()
        self.window.mainloop()

    def frames_init(self):
        self.top_frame.grid()
        self.bottom_frame.grid()

    def submit_button(self):
        self.submit = Button(self.bottom_frame, text='Submit', fg='Black', bg='White', command=self.label_update)
        self.submit.grid(row=10, column=2)

    def clear_button(self):
        self.clear = Button(self.bottom_frame, text='Clear the board', fg='Black', bg='White', command='Clear')
        self.clear.grid(row=10, column=1)

    def label_init(self):
        self.label = Label(self.top_frame, text='This is fun Sudoku Game!')
        self.label.grid(row=0, columnspan=9)
        self.label2 = Label(self.bottom_frame, text= f'{self.gameboard[0]} \n {self.gameboard[1]} \n {self.gameboard[2]}')
        self.label2.grid(row=12, column=0, columnspan=10, rowspan=5)
    def label_update(self):
        for i in range(1, len(self.game.board) + 1):
            for j in range(1, len(self.game.board) + 1):
                try:
                    self.gameboard1[i - 1][j - 1] = self.gameboard[i - 1][j - 1].get()
                except(AttributeError):
                    pass

        self.gameboard = [[item.get() for item in self.gameboard]]
        self.label2 = Label(self.bottom_frame,
                            text=f'{self.gameboard1[0]} \n {self.gameboard1[1]} \n {self.gameboard1[2]}')
        self.label2.grid(row=12, column=0, columnspan=10, rowspan=5)

    # def entry_box(self):
    #     self.entry = Entry(self.window)
    #
    def board_creation(self):
        # self.entry1 = Entry()
        # self.entry2 = Entry()
        # self.entry3 = Entry()
        # self.entry4 = Entry()
        # self.entry5 = Entry()
        # self.entry6 = Entry()
        # self.entry7 = Entry()
        # self.entry8 = Entry()
        # self.entry9 = Entry()
        # self.entry1.grid(row=1, column=1)
        # self.entry2.grid(row=1, column=2)
        # self.entry3.grid(row=1, column=3)
        # self.entry4.grid(row=2, column=1)
        # self.entry5.grid(row=2, column=2)
        # self.entry6.grid(row=2, column=3)
        # self.entry7.grid(row=3, column=1)
        # self.entry8.grid(row=3, column=2)
        # self.entry9.grid(row=3, column=3)
        # i = 0
        # j = 0
        # for item in self.gameboard:
        #     item.grid(row=j, column=i)
        #     i += 1
        #     if i == 3:
        #         i = 0
        #         j += 1
        for i in range(1, len(self.game.board) + 1):
            for j in range(1, len(self.game.board) + 1):
                self.gameboard[i - 1][j - 1] = Entry(self.top_frame, width=2).grid(row=i, column=j)

    def board_status(self):
        for i in range(1, len(self.game.board) + 1):
            for j in range(1, len(self.game.board) + 1):
                try :
                    self.gameboard[i - 1][j - 1].get()
                except(AttributeError):
                    pass
    def change_num(self):
        self.num += 1
if __name__ == '__main__':

    GameInterface = SudokuInterface()
    GameInterface.game_interface()
