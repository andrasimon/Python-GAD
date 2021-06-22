# py TicTacToe.py
from os import system


def ClearScreen():
    cls = lambda: system('cls')
    cls()


class TicTacToe:
    def __init__(self):
        self.board = {7: ' ', 8: ' ', 9: ' ',
                      4: ' ', 5: ' ', 6: ' ',
                      1: ' ', 2: ' ', 3: ' '
                      }
        self.numkey = {7: '7', 8: '8', 9: '9',
                       4: '4', 5: '5', 6: '6',
                       1: '1', 2: '2', 3: '3'
                       }
        self.winner = ''
        self.status = 'y'
        self.role = ''
        self.game_over = 0

    def StartGame(self):
        print('Game started!\nHere are some instructions.\nUse your Num Keyboard (numbers from 1 to 9) '
              'to identify each box on the board,\n'
              'then insert the number of the position you aim for.')
        self.role = '0'
        self.game_over = 0

    def ResetBoard(self):
        self.board = {7: ' ', 8: ' ', 9: ' ',
                      4: ' ', 5: ' ', 6: ' ',
                      1: ' ', 2: ' ', 3: ' '
                      }

    def FillBoard(self):
        try:
            move = input('What\'s your move?  ')
            ClearScreen()
            if self.board[int(move)] not in ('X', '0'):
                self.board[int(move)] = self.role
            else:
                print('That was an invalid move, {}! You missed your turn!'.format(self.role))
        except ValueError:
            print('That\'s an invalid input! You missed your turn!')

    def CheckBoard(self):
        if self.board[7] == self.board[8] == self.board[9] != ' ':
            self.winner = self.board[7]
            self.FinishGame()
        if self.board[4] == self.board[5] == self.board[6] != ' ':
            self.winner = self.board[4]
            self.FinishGame()
        if self.board[1] == self.board[2] == self.board[3] != ' ':
            self.winner = self.board[1]
            self.FinishGame()
        if self.board[7] == self.board[4] == self.board[1] != ' ':
            self.winner = self.board[7]
            self.FinishGame()
        if self.board[8] == self.board[5] == self.board[2] != ' ':
            self.winner = self.board[8]
            self.FinishGame()
        if self.board[9] == self.board[6] == self.board[3] != ' ':
            self.winner = self.board[9]
            self.FinishGame()
        if self.board[7] == self.board[5] == self.board[3] != ' ':
            self.winner = self.board[7]
            self.FinishGame()
        if self.board[9] == self.board[5] == self.board[1] != ' ':
            self.winner = self.board[9]
            self.FinishGame()
        if ' ' not in self.board.values():
            self.winner = 'Nobody'
            self.FinishGame()

    def SwitchRole(self):
        if self.role == 'X':
            self.role = '0'
        else:
            self.role = 'X'
        print('\nIt\'s {}\'s turn.'.format(self.role))

    def PrintBoard(self):
        print('Here is the board.\n\n {} | {} | {} \n---+---+---\n {} | {} | {} \n---+---+---\n {} | {} | {} '.format(
            self.board[7], self.board[8], self.board[9],
            self.board[4], self.board[5], self.board[6],
            self.board[1], self.board[2], self.board[3]
        ))

    def PrintNumKeyboard(self):
        print('This board is here for your orientation.\n\n {} | {} | {} \n---+---+---\n {} | {} | {} \n---+---+---\n'
              ' {} | {} | {} \n'.format(self.numkey[7], self.numkey[8], self.numkey[9],
                                        self.numkey[4], self.numkey[5], self.numkey[6],
                                        self.numkey[1], self.numkey[2], self.numkey[3]
        ))

    def FinishGame(self):
        self.game_over = 1
        self.PrintBoard()
        print('\nGame over! It looks like {} won!'.format(self.winner))
        self.status = input('Want to play again? y/n ')
        while self.status.upper() not in ('N', 'Y'):
            self.status = input('That was invalid input! Want to play again? y/n ')


if __name__ == '__main__':
    game = TicTacToe()
    while game.status.upper() == 'Y':
        ClearScreen()
        game.StartGame()
        while game.game_over == 0:
            game.PrintNumKeyboard()
            game.PrintBoard()
            game.SwitchRole()
            game.FillBoard()
            game.CheckBoard()
        game.ResetBoard()
    print('Thanks for playing!')
