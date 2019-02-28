class TicTacToe():
    def __init__(self):
        self.board = [['-'] * 3 for _ in range(3)]
        self.player_ones_turn = True
        self.quit_commands = ['Q', 'q']
        self.game_over = False

# -- player methods --
    def get_current_player(self):
        if self.player_ones_turn:
            return 1
        return 2

    def toggle_current_player(self):
        self.player_ones_turn = not self.player_ones_turn

    def check_user_quit(self, input):
        if input in self.quit_commands:
            self.quit_game()

# -- end game methods --

    def quit_game(self):
        self.print_quit_screen()
        self.game_over = True

    def won(self):
        self.print_winning_screen()
        self.game_over = True

    def draw(self):
        self.print_draw_screen()
        self.game_over = True


# -- token methods --
    def add_token(self, row, col, token):
        self.board[row][col] = token

    def get_token(self):
        if self.player_ones_turn:
            return 'X'
        return 'O'

# -- validation methods --
    def is_game_over(self):
        return self.game_over

    def is_valid_move(self, row, col):
        if row in [0, 1, 2] and col in [0, 1, 2] and self.board[row][col] == '-':
            return True
        return False

# -- finished game methods --
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
            if row == 0:
                print('0 1 2')
            for col in range(3):
                print(self.board[row][col], end='')
                if col < 2:
                    print('|', end = '')
                else:
                    print(' {}'.format(row))
        print()

    def print_welcome_screen(self):
        print('=====// Tic Tac Toe //=====\n')
        print('Welcome! We are happy to see you ╰(◕ᗜ◕)╯')
        if input('Would you like instructions on how to play? (yes/no) ') == 'yes':
            self.print_instructions()
        print("Okay! Let's begin!\n")
        self.print_board()

    def print_instructions(self):
        instructions = """
            This is a two player game
            The first player to fill a row, column or diagonal wins!
            Player 1 has the X token
            Player 2 has the O token
            To place a token, first type the column (down) you would like to select
            Then the row (across)
            Columns and rows are numbered 0 - 2
            Player 1 goes first.
            Press Q at any time to quit
        """
        print(instructions)

    def print_next_move_screen(self):
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
    while not board.is_game_over():

        col = input('Please type the column [0-2]: ')

        board.check_user_quit(col)
        if board.is_game_over():
            break

        row = input('Please type the row [0-2]: ')

        board.check_user_quit(row)
        if board.is_game_over():
            break

        #come back to this
        row, col = int(row), int(col)
        if board.is_valid_move(row, col):

            token = board.get_token()
            board.add_token(row, col, token)

            if board.is_winning_move(row, col, token):
                board.won()

            elif board.is_full():
                board.draw()

            else:
                board.toggle_current_player()
                board.print_next_move_screen()

        else:
            board.print_invalid_screen()
main()
