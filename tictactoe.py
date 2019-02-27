class TicTacToe():
    def __init__(self):
        self.board = [['-'] * 3 for _ in range(3)]

    def printBoard(self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col], end='')
                if col < 2:
                    print('|', end = '')
                else:
                    print(' ')





def main():
    myBoard = TicTacToe()
    myBoard.printBoard()

main()
