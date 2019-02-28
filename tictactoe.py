class TicTacToe():
    def __init__(self):
        self.board = [['-'] * 3 for _ in range(3)]
        self.player_ones_turn = True

# -- player methods --
    def get_current_player(self):
        if self.player_ones_turn:
            return 1
        return 2

    def toggle_current_player(self):
        self.player_ones_turn = not self.player_ones_turn

# -- token methods --
    def add_token(self, row, col, token):
        self.board[row][col] = token

    def get_token(self):
        if self.player_ones_turn:
            return 'X'
        return 'O'

# -- validation methods --
    def is_valid_move(self, row, col):
        try:
            row = int(row)
            col = int(col)
        except:
            return False

        if row in [0, 1, 2] and col in [0, 1, 2] and self.board[row][col] == '-':
            return True
        return False

    def is_winning_move(self, row, col, token):
        #check row
        if self.filled_row(row, token):
            return True
        elif self.filled_column(col, token):
            return True
        elif row == col or row + col == 2:
            return self.filled_diagonal(row, col, token)

        return False

    def filled_row(self, row, token):
        for x in range(3):
            if self.board[row][x] != token:
                break
            if x == 2:
                return True
        return False

    def filled_column(self, col, token):
        for y in range(3):
            if self.board[y][col] != token:
                break
            if y == 2:
                return True
        return False

    def filled_diagonal(self, row, col, token):
        for diag in range(3):
            if self.board[diag][diag] != token:
                break
            if diag == 2:
                return True

        for diag in range(3):
            if self.board[diag][2-diag] != token:
                break
            if diag == 2:
                return True
        return False


    def is_full(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '-':
                    return False
        return True


# -- print methods --
    def print_board(self):
        print('\n====// Board //=====\n')
        for row in range(3):
            for col in range(3):
                print(self.board[row][col], end='')
                if col < 2:
                    print('|', end = '')
                else:
                    print(' ')
        print()

    def print_welcome_screen(self):
        print('=====// Tic Tac Toe //=====\n')
        print('Welcome! We are happy to see you ╰(◕ᗜ◕)╯')
        if input('Would you like instructions on how to play? (yes/no) ') == 'yes':
            self.print_instructions()
        print("Okay! Let's begin!\n")

    def print_instructions(self):
        instructions = """
            This is a two player game
            The first player to fill a row, column or diagonal wins!
            Player 1 has the X token
            Player 2 has the O token
            To place a token, first type the row you would like to select
            Then the column
            Columns and rows are numbered 0 - 2
            Player 1 goes first.
            Press Q at any time to quit
        """
        print(instructions)

    def print_header(self):
        self.print_board()
        print("=====// Your Turn Player {} //=====\n".format(self.get_current_player()))

    def print_winning_screen(self):
        self.print_board()
        print('\n=====// Player {} won the game ! ! ! //====='.format(self.get_current_player()))
        print('╰(✿˙ᗜ˙)੭━☆ﾟ.*･｡ﾟ')

    def print_draw_screen(self):
        self.print_board()
        print('\n=====// The game was a draw! //=====')
        print('༼ ⨀ ̿Ĺ̯̿̿⨀ ̿༽ง\n')

    def print_quit_screen(self):
        print('\nYou quit the game! We hope to see you again soon!')
        print('Goodbye! c( ⁰ 〰 ⁰ )੭\n')

    def print_invalid_screen(self):
        print('\nInvalid move player {} (-_-｡) Please try again\n'.format(self.get_current_player()))


def main():
    board = TicTacToe()
    board.print_welcome_screen()
    while True:
        board.print_header()
        row = input('Please type the row [0-2]: ')
        if row == 'Q' or row == 'q':
            board.print_quit_screen()
            break

        col = input('Please type the column [0-2]: ')
        if col == 'Q' or row == 'q':
            board.print_quit_screen()
            break

        if board.is_valid_move(row, col):
            ###clean this next line up .. & make input sanitizing robust
            ###change from 0-2 to 1-9?
            row, col = int(row), int(col)

            token = board.get_token()
            board.add_token(row, col, token)

            if board.is_winning_move(row, col, token):
                board.print_winning_screen()
                break

            if board.is_full():
                board.print_draw_screen()
                break

            board.toggle_current_player()

        else:
            board.print_invalid_screen()
main()
