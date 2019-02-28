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

    def user_quit(self, input):
        if input in self.quit_commands:
            self.quit_game()
            return True
        return False

# -- end game methods --
    def is_game_over(self):
        return self.game_over

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

# -- input validation methods --
    def validate_input(self, input):
        try:
            input = int(input)
        except:
            return -1

        if input in [0, 1, 2]:
            return input
        return -1

    def is_valid_move(self, row, col):
        if self.board[row][col] == '-':
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
        print('\n=====// Board //=====\n')
        for row in range(3):
            if row == 0:
                print('0 1 2\n')
            for col in range(3):
                print(self.board[row][col], end='')
                if col < 2:
                    print('|', end = '')
                else:
                    print('   {}'.format(row))
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

            To place a token, first type the column (down), then the row (across)
            Columns and rows are numbered 0 - 2
            Press q or Q any time to quit

            Player 1 goes first.
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
        print('\nYou quit the game! We hope to see you again soon')
        print('c( ⁰ 〰 ⁰ )੭\n')

    def print_invalid_screen(self):
        print('\n! Invalid move player {} ! (-_-｡)\n\nPlease try again\n'.format(self.get_current_player()))


def main():
    
    board = TicTacToe()
    board.print_welcome_screen()

    while not board.is_game_over():
        board.print_next_move_screen()

        col = input('Column [0-2]: ')

        if board.user_quit(col):
            continue

        row = input('Row [0-2]: ')

        if board.user_quit(row):
            continue

        row, col = board.validate_input(row), board.validate_input(col)

        if row == -1 or col == -1 or not board.is_valid_move():
            board.print_invalid_screen()

        else:
            token = board.get_token()
            board.add_token(row, col, token)

            if board.is_winning_move(row, col, token):
                board.won()

            elif board.is_full():
                board.draw()

            board.toggle_current_player()
main()
