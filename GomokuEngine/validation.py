from GomokuEngine.gomokuTypes import Player, DIM, MAX_TURNS
import numpy as np

class Validate:
    @staticmethod
    def isFieldEmpty(x, y, board):
        return board[y][x] == Player.EMPTY

    @staticmethod
    def isOnField(x, y):
        return 0 <= x < DIM and \
               0 <= y < DIM

    @staticmethod
    def isValidMove(x, y, board):
        return Validate.isOnField(x, y) and \
               Validate.isFieldEmpty(x, y, board)

    @staticmethod
    def checkRow(x):
        sum = 0
        player = Player.EMPTY
        for elem in x:
            if elem != player:
                if sum == 5 and player != Player.EMPTY: return player
                player = elem
                sum = 0
            sum += 1
        else:
            if sum == 5: return player
        return Player.EMPTY

    @staticmethod
    def checkRows(board):
        for y in board:
            result = Validate.checkRow(y)
            if result != Player.EMPTY: return result

    @staticmethod
    def checkColumns(board):
        for x in board.transpose():
            result = Validate.checkRow(x)
            if result != Player.EMPTY: return result

    @staticmethod
    def checkDiagonalsInternal(data):
        offset_row = 1 - data.shape[0]
        offset_column = data.shape[1]
        for offst in range(offset_row, offset_column):
            result = Validate.checkRow(data.diagonal(offset=offst))
            if not result == Player.EMPTY:
                return result

    @staticmethod
    def checkDownwardsDiagonals(board):
        return Validate.checkDiagonalsInternal(board)

    @staticmethod
    def checkUpwardsDiagonals(board):
        return Validate.checkDiagonalsInternal(np.fliplr(board))

    @staticmethod
    def checkDraw(turns):
        return turns == MAX_TURNS

    @staticmethod
    def checkWinner(board):
        funcs = [
            Validate.checkRows,
            Validate.checkColumns,
            Validate.checkDownwardsDiagonals,
            Validate.checkUpwardsDiagonals
        ]
        for func in funcs:
            result = func(board)
            if result: return result
        return Player.EMPTY

    @staticmethod
    def isGameOver(turns, board):
        return Validate.checkDraw(turns) or Validate.checkWinner(board) != Player.EMPTY

    @staticmethod
    def print(board):
        playerToChar = {
            Player.WHITE: 'W',
            Player.EMPTY: '.',
            Player.BLACK: 'B'}
        print('\t', end='')
        [print(x, end='\t') for x in range(DIM)]
        print()
        for idxY, y in enumerate(board):
            print(idxY, end='\t')
            for x in y:
                print(playerToChar[x], end='\t')
            print()