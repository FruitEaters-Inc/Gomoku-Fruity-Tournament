from GomokuEngine.gomoku import Board
from GomokuEngine.agents.human import HumanAgent
if __name__ == '__main__':
    board = Board([HumanAgent(), HumanAgent()])
    board.startGame()