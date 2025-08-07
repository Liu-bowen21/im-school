class TicTacToe:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.player = 'O'
        self.game_over = False


    def print_board(self):
        """
        This function makes the board
        params:
        None
        returns:
        None
        """
        for row in self.board:
            print(' '.join(row))
        print()


    def check_winner(self):
        """
        This function makes sure that check the winner
        params:
        None
        returns:
        - bool true if have a winner, false otherwise  
        """
        b = self.board
        lines = b + [[b[r][c] for r in range(3)] for c in range(3)] + \
                [[b[i][i] for i in range(3)]] + [[b[i][2 - i] for i in range(3)]]
        return any(line[0] != '-' and all(cell == line[0] for cell in line) for line in lines)

    def is_full(self):
        """
        This function makes sure that check all the position have X or O
        params:
        None
        returns:
        - bool true if the board is full,false otherwise
        """
        return all(cell != '-' for row in self.board for cell in row)

    def is_game_over(self):
        """
        This function makes sure that who win
        params:
        None
        returns:
        None
        """
        if self.check_winner():
            print(f"Player{self.player}win")
            self.game_over = True
        elif self.is_full():
            print("It's a tie")
            self.game_over = True


    def place_marker(self):
        """
        This function makes sure that let the player put the X or O in the board
        params:
        None
        returns:
        None
        """
        row = int(input("Row (0-2): "))
        col = int(input("Col (0-2): "))
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == '-':
            self.board[row][col] == '-'
            if self.player == 'X':
                self.board[row][col] = 'O'
                self.player = 'O'
            else:
                self.board[row][col] = 'X'
                self.player = 'X'
        else:
            print("You cannot put that there!")
        

    def play_game(self):
        """
        This function makes sure that game start is playerX first
        params:
        None
        returns:
        None
        """
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
