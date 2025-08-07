import random

class TicTacToe:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Human is 'X', AI is 'O'
        self.game_over = False

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def check_winner(self):
        b = self.board
        lines = b + [[b[r][c] for r in range(3)] for c in range(3)] + \
                [[b[i][i] for i in range(3)]] + [[b[i][2 - i] for i in range(3)]]
        for line in lines:
            if line[0] != '-' and all(cell == line[0] for cell in line):
                return line[0]
        return None

    def is_full(self):
        return all(cell != '-' for row in self.board for cell in row)

    def ai_move(self, ai_player):
        print(f"AI ({ai_player}) is making a move...")
        # 1. Check for immediate win
        moves = [(r, c) for r in range(3) for c in range(3)]
        random.shuffle(moves)
        for r, c in moves:
            if self.board[r][c] == '-':
                self.board[r][c] = ai_player
                if self.check_winner() == ai_player:
                    return
                self.board[r][c] = '-'
        # 2. Block opponent's immediate win
        opponent = 'O' if ai_player == 'X' else 'X'
        random.shuffle(moves)
        for r, c in moves:
            if self.board[r][c] == '-':
                self.board[r][c] = opponent
                if self.check_winner() == opponent:
                    self.board[r][c] = ai_player
                    return
                self.board[r][c] = '-'
        # 3. Use minimax for best move
        best_score = -float('inf')
        best_move = None
        random.shuffle(moves)
        for r, c in moves:
            if self.board[r][c] == '-':
                self.board[r][c] = ai_player
                score = self.minimax(ai_player == 'O', -float('inf'), float('inf'), ai_player)
                self.board[r][c] = '-'
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
        if best_move:
            r, c = best_move
            self.board[r][c] = ai_player


    def minimax(self, is_ai, alpha, beta, ai_player):
        winner = self.check_winner()
        if winner == ai_player:
            return 1
        elif winner == ('O' if ai_player == 'X' else 'X'):
            return -1
        elif self.is_full():
            return 0
        moves = [(r, c) for r in range(3) for c in range(3)]
        random.shuffle(moves)
        if is_ai:
            best_score = -float('inf')
            for r, c in moves:
                if self.board[r][c] == '-':
                    self.board[r][c] = ai_player
                    score = self.minimax(False, alpha, beta, ai_player)
                    self.board[r][c] = '-'
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
            return best_score
        else:
            best_score = float('inf')
            opponent = 'O' if ai_player == 'X' else 'X'
            for r, c in moves:
                if self.board[r][c] == '-':
                    self.board[r][c] = opponent
                    score = self.minimax(True, alpha, beta, ai_player)
                    self.board[r][c] = '-'
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
            return best_score

    def random_move(self, player):
        print(f"Random AI ({player}) is making a move...")
        moves = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == '-']
        if moves:
            r, c = random.choice(moves)
            self.board[r][c] = player

    def play_game(self):
        print("TicTacToe: Random X vs Random O! X goes first.")
        self.print_board()
        while not self.game_over:
            self.random_move(self.current_player)
            import time
            time.sleep(2)
            self.print_board()
            winner = self.check_winner()
            if winner:
                print(f"{winner} wins!")
                self.game_over = True
            elif self.is_full():
                print("It's a tie!")
                self.game_over = True
            self.current_player = 'O' if self.current_player == 'X' else 'X'

if __name__ == "__main__":
    print("Choose mode:")
    print("1: Human vs AI")
    print("2: Human vs Human")
    print("3: AI vs AI")
    mode = input("Enter 1, 2, or 3: ").strip()
    human_player = None
    if mode == '1':
        print("Do you want to play as X or O?")
        human_player = input("Enter X or O: ").strip().upper()
        if human_player not in ['X', 'O']:
            print("Invalid choice, defaulting to X.")
            human_player = 'X'

    def get_human_move(board, player):
        while True:
            try:
                move_str = input(f"{player} move (row col, e.g. 0 1): ").strip()
                row, col = map(int, move_str.split())
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '-':
                    return row, col
                else:
                    print("Invalid move. Try again.")
            except Exception:
                print("Invalid input. Try again.")

    game = TicTacToe()
    game.print_board()
    if mode == '1':
        while not game.game_over:
            if game.current_player == human_player:
                row, col = get_human_move(game.board, human_player)
                game.board[row][col] = human_player
            else:
                ai_player = 'O' if human_player == 'X' else 'X'
                game.ai_move(ai_player)
            game.print_board()
            winner = game.check_winner()
            if winner:
                print(f"{winner} wins!")
                game.game_over = True
            elif game.is_full():
                print("It's a tie!")
                game.game_over = True
            game.current_player = 'O' if game.current_player == 'X' else 'X'
    elif mode == '2':
        while not game.game_over:
            row, col = get_human_move(game.board, game.current_player)
            game.board[row][col] = game.current_player
            game.print_board()
            winner = game.check_winner()
            if winner:
                print(f"{winner} wins!")
                game.game_over = True
            elif game.is_full():
                print("It's a tie!")
                game.game_over = True
            game.current_player = 'O' if game.current_player == 'X' else 'X'
    else:
        game.play_game()