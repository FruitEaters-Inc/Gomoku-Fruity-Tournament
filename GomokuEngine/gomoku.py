from GomokuEngine.validation import Validate
from GomokuEngine.gomokuTypes import *
import numpy as np

isSameSign = lambda x, y: x * y > 0

class Board:
    def __init__(self, players):
        assert(len(players) == 2)
        self.winner = Player.EMPTY
        self.currentTurn = 0
        self.board = np.array([[Player.EMPTY for x in range(DIM)] for y in range(DIM)])
        self.players = players

    def startGame(self):
        i = 0
        self.openingStage()
        while not Validate.isGameOver(self.currentTurn, self.board):
            self.setField(self.players[i].move(self.board, [Player.BLACK, Player.WHITE][i]))
            i = 0 if i else 1
        return Validate.checkWinner(self.board)

    def swapPlayers(self):
        self.players[0], self.players[1] = self.players[1], self.players[0]

    def setFields(self, moves):
        for move in moves: self.setField(move)

    def openingStage(self):
    #three first stones are set by first player
        self.setFields(self.players[0].openingThree(self.board))
        
    #second move is:
    #->color swap
    #->adding two stones
        if self.players[1].askColorChange(self.board):
            if self.players[1].changeColor(self.board) == Player.BLACK: self.swapPlayers()
        else:
            self.setFields(self.players[1].openingTwo(self.board))
            self.players[0].changeColor(self.board)
            if self.players[1].colorChange(self.board) == Player.WHITE: self.swapPlayers()
    
        #move is tuple in form of [x, y, player]
    def setField(self, move):
        x, y, player = move
        assert(Validate.isValidMove(x, y, self.board))
        self.board[y][x] = player
        self.currentTurn += 1