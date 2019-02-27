class TicTacToe():
    def __init__(self):
        self.board = [['-'] * 3 for _ in range(3)]
        self.player_one_moves = True

# -- player methods --
    def get_current_player(self):
        if self.player_one_moves:
            return 1
        return 2

    def toggle_current_player(self):
        self.player_one_moves = not self.player_one_moves

# -- token methods --
    def add_token(self, row, col, token):
        self.board[row][col] = token

# -- validation methods --
    def is_valid_move(self, row, col):
        if self.board[row][col] == '-':
            return True
        return False

    def check_for_winning_move(self):
        if self.player_one_moves:
            token = 'X'
        else:
            token = 'O'

        ### finish..

    def check_board_is_full(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '-':
                    return False
        return True


# -- print methods --
    def print_board (self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col], end='')
                if col < 2:
                    print('|', end = '')
                else:
                    print(' ')

    def print_header(self):
        board.print_board()
        print("=====//Player {}//=====".format(board.get_current_player()))


def main():
    board = TicTacToe()
    while not board.check_board_is_full():
        board.print_header()
        row, col = int(input('Please type the row [0-2]: ')), int(input('Please type the column [0-2]: '))
        if board.is_valid_move(row, col):
            if board.get_current_player() == 1:
                token = 'X'
            else:
                token = 'O'
            board.add_token(row, col, token)
            board.toggle_current_player()

        else:
            print('Invalid move player {}. Please try again'.format(board.get_current_player()))

main()
