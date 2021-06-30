from gomoku import *

class TestBoardClass(unittest.TestCase):
    def setUp(self):
        self.board = Board(15)

    def testInit(self):
        self.assertEqual(len(self.board.board), 15)
        for i in self.board.board:
            self.assertEqual(len(i), 15)

    def testIsFieldEmpty(self):
        self.assertTrue(self.board.isFieldEmpty(0,0))

    def testSetField(self):
        self.board.setField(1, 0, Player.WHITE)
        self.assertTrue(self.board.board[0][1], Player.WHITE)

    def testCheckWinnerHorizonalCase0(self):
        for i in range(7, 12):
            self.board.setField(i, 1, Player.WHITE)

        self.assertEqual(self.board.checkWinner(), Player.WHITE)

    def testCheckWinnerHorizonalEdgeCase0(self):
        for i in range(10, 15):
            self.board.setField(i, 0, Player.WHITE)
        
        self.assertEqual(self.board.checkWinner(), Player.WHITE)

    def testCheckWinnerHorizonalEdgeCase1(self):
        for i in range(5):
            self.board.setField(i, 0, Player.BLACK)

        self.assertEqual(self.board.checkWinner(), Player.BLACK)

    def testCheckWinnerHorizonalEdgeCase2(self):
        for i in range(6):
            self.board.setField(i, 0, Player.BLACK)
            
        self.assertEqual(self.board.checkWinner(), Player.EMPTY)

    def testCheckWinnerHorizonalEdgeCase3(self):
        for i in range(11,15):
            self.board.setField(i, 0, Player.BLACK)
            
        self.assertEqual(self.board.checkWinner(), Player.EMPTY)

    def testCheckWinnerVerticalEdgeCase0(self):
        for i in range(10, 15):
            self.board.setField(0, i, Player.WHITE)
        
        self.assertEqual(self.board.checkWinner(), Player.WHITE)

    def testCheckWinnerVerticalEdgeCase1(self):
        for i in range(9, 15):
            self.board.setField(0, i, Player.WHITE)
        
        self.assertEqual(self.board.checkWinner(), Player.EMPTY)

    def testCheckWinnerVerticalCase0(self):
        for i in range(5, 10):
            self.board.setField(2, i, Player.BLACK)
        
        self.assertEqual(self.board.checkWinner(), Player.BLACK)
     
    def testCheckWinnerDownwardsDiagonal(self):
        for i in range(5, 10):
            self.board.setField(i, i, Player.BLACK)
        self.assertEqual(self.board.checkWinner(), Player.BLACK)

    def testCheckWinnerUpwardsDiagonal(self):
        for i in range(5, 10):
            self.board.setField(i, self.board.boardDimensions - i, Player.BLACK)
        self.assertEqual(self.board.checkWinner(), Player.BLACK)

    def testIsValidMove(self):
        self.assertFalse(self.board.isValidMove(0, 0))
        self.assertTrue(self.board.isValidMove(7, 7))
        self.board.setField(7, 7, Player.BLACK)
        self.assertTrue(self.board.isValidMove(1, 1))
        self.board.setField(4, 4, Player.WHITE)
        self.assertFalse(self.board.isValidMove(4, 4))
        self.assertFalse(self.board.isValidMove(6, 6))
        self.assertTrue(self.board.isValidMove(2, 2))
        self.assertFalse(self.board.isValidMove(-1, -1))
        self.assertFalse(self.board.isValidMove(3, 20))
        
if __name__ == '__main__':
    unittest.main()