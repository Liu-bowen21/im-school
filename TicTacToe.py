class TicTacToe:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.game_over = False


    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3:
            if self.board[row][col] == '-':
                self.board[row][col] = self.player
                return True
            else:
                print("Cell already taken.")
        else:
            print("Invalid move: row and column must be 0-2.")
        return False


    def check_winner(self):
        b = self.board
        lines = b + [[b[r][c] for r in range(3)] for c in range(3)] + \
                [[b[i][i] for i in range(3)]] + [[b[i][2 - i] for i in range(3)]]
        return any(line[0] != '-' and all(cell == line[0] for cell in line) for line in lines)

    def is_full(self):
        return all(cell != '-' for row in self.board for cell in row)

    def is_game_over(self):
        if self.check_winner():
            print(f"Player{self.player}win!")
            self.game_over = True
        elif self.is_full():
            print("It's a tie")
            self.game_over = True


    def place_marker(self):
        row = int(input("Row (0-2): "))
        col = int(input("Col (0-2): "))
        if self.board[row][col] == '-':
            if self.player == 'X':
                self.board[row][col] = 'O'
                self.player = 'O'
            else:
                self.board[row][col] = 'X'
                self.player = 'X'
        else:
            print("You cannot put that there!")


    def play_game(self):
        self.turn = 'playerX'
        while self.game_over is False:
            self.place_marker()
            self.print_board()
            self.is_game_over()
            self.turn = 'playerO'



tictactoe = TicTacToe()
tictactoe.print_board()


if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.play_game()
