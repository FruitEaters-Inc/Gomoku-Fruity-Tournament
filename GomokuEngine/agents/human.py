from GomokuEngine.validation import Validate
from .base import BaseAgent
from GomokuEngine.gomokuTypes import Player

class HumanAgent(BaseAgent):
    def __init__(self) -> None:
        self.color = None
        super().__init__()

    def openingThree(self, board):
        return (
            (int(input("podaj x-> ")),int(input("podaj y-> ")), Player.BLACK),
            (int(input("podaj x-> ")),int(input("podaj y-> ")), Player.BLACK),
            (int(input("podaj x-> ")),int(input("podaj y-> ")), Player.WHITE)
        )

    def openingTwo(self, board):
        Validate.print(board)
        return (
            (int(input("podaj x-> ")),int(input("podaj y-> ")), Player.BLACK),
            (int(input("podaj x-> ")),int(input("podaj y-> ")), Player.WHITE)
        )

    def move(self, board, color):
        Validate.print(board)
        self.color = color
        print("your color is ", self.color)
        return int(input("podaj x-> ")),int(input("podaj y-> ")), color

    def askColorChange(self, board):
        Validate.print(board)
        return input("chcesz zmienic kolor?") == 't'

    def changeColor(self, board):
        Validate.print(board)
        return Player.WHITE if input("bialy?(jesli nie to czarny)") == 't' else Player.BLACK
