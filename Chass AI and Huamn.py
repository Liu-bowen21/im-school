
import random
# Simple Chess Board Representation
# This is a basic chess board and piece setup in Python

class ChessBoard:
    def get_winner(self):
        white_king = any('K' in row for row in self.board)
        black_king = any('k' in row for row in self.board)
        if not white_king:
            return 'black'
        if not black_king:
            return 'white'
        return None
    def get_piece_moves(self, color):
        moves = []
        captures = []
        piece_sets = {
            'white': {'P','R','N','B','Q','K'},
            'black': {'p','r','n','b','q','k'}
        }
        enemy = {'white': {'p','r','n','b','q','k'}, 'black': {'P','R','N','B','Q','K'}}
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece in piece_sets[color]:
                    # Pawn moves (already handled)
                    if piece == 'P':
                        if r > 0 and self.board[r-1][c] == '-':
                            moves.append(((r, c), (r-1, c)))
                        if r > 0 and c > 0 and self.board[r-1][c-1] in enemy[color]:
                            captures.append(((r, c), (r-1, c-1)))
                        if r > 0 and c < 7 and self.board[r-1][c+1] in enemy[color]:
                            captures.append(((r, c), (r-1, c+1)))
                    elif piece == 'p':
                        if r < 7 and self.board[r+1][c] == '-':
                            moves.append(((r, c), (r+1, c)))
                        if r < 7 and c > 0 and self.board[r+1][c-1] in enemy[color]:
                            captures.append(((r, c), (r+1, c-1)))
                        if r < 7 and c < 7 and self.board[r+1][c+1] in enemy[color]:
                            captures.append(((r, c), (r+1, c+1)))
                    # Rook moves
                    elif piece in {'R','r'}:
                        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            for i in range(1,8):
                                nr, nc = r+dr*i, c+dc*i
                                if 0<=nr<8 and 0<=nc<8:
                                    if self.board[nr][nc] == '-':
                                        moves.append(((r,c),(nr,nc)))
                                    elif self.board[nr][nc] in enemy[color]:
                                        captures.append(((r,c),(nr,nc)))
                                        break
                                    else:
                                        break
                    # Bishop moves
                    elif piece in {'B','b'}:
                        for dr, dc in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                            for i in range(1,8):
                                nr, nc = r+dr*i, c+dc*i
                                if 0<=nr<8 and 0<=nc<8:
                                    if self.board[nr][nc] == '-':
                                        moves.append(((r,c),(nr,nc)))
                                    elif self.board[nr][nc] in enemy[color]:
                                        captures.append(((r,c),(nr,nc)))
                                        break
                                    else:
                                        break
                    # Queen moves
                    elif piece in {'Q','q'}:
                        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                            for i in range(1,8):
                                nr, nc = r+dr*i, c+dc*i
                                if 0<=nr<8 and 0<=nc<8:
                                    if self.board[nr][nc] == '-':
                                        moves.append(((r,c),(nr,nc)))
                                    elif self.board[nr][nc] in enemy[color]:
                                        captures.append(((r,c),(nr,nc)))
                                        break
                                    else:
                                        break
                    # Knight moves
                    elif piece in {'N','n'}:
                        for dr, dc in [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]:
                            nr, nc = r+dr, c+dc
                            if 0<=nr<8 and 0<=nc<8:
                                if self.board[nr][nc] == '-':
                                    moves.append(((r,c),(nr,nc)))
                                elif self.board[nr][nc] in enemy[color]:
                                    captures.append(((r,c),(nr,nc)))
                    # King moves
                    elif piece in {'K','k'}:
                        for dr in [-1,0,1]:
                            for dc in [-1,0,1]:
                                if dr==0 and dc==0:
                                    continue
                                nr, nc = r+dr, c+dc
                                if 0<=nr<8 and 0<=nc<8:
                                    if self.board[nr][nc] == '-':
                                        moves.append(((r,c),(nr,nc)))
                                    elif self.board[nr][nc] in enemy[color]:
                                        captures.append(((r,c),(nr,nc)))
        return captures if captures else moves
    def get_pawn_moves(self, color):
        moves = []
        captures = []
        if color == 'white':
            for r in range(8):
                for c in range(8):
                    if self.board[r][c] == 'P':
                        # Forward move
                        if r > 0 and self.board[r-1][c] == '-':
                            moves.append(((r, c), (r-1, c)))
                        # Capture left
                        if r > 0 and c > 0 and self.board[r-1][c-1] == 'p':
                            captures.append(((r, c), (r-1, c-1)))
                        # Capture right
                        if r > 0 and c < 7 and self.board[r-1][c+1] == 'p':
                            captures.append(((r, c), (r-1, c+1)))
        else:
            for r in range(8):
                for c in range(8):
                    if self.board[r][c] == 'p':
                        # Forward move
                        if r < 7 and self.board[r+1][c] == '-':
                            moves.append(((r, c), (r+1, c)))
                        # Capture left
                        if r < 7 and c > 0 and self.board[r+1][c-1] == 'P':
                            captures.append(((r, c), (r+1, c-1)))
                        # Capture right
                        if r < 7 and c < 7 and self.board[r+1][c+1] == 'P':
                            captures.append(((r, c), (r+1, c+1)))
        # Prefer captures if available
        return captures if captures else moves

    def make_move(self, move):
        (r1, c1), (r2, c2) = move
        self.board[r2][c2] = self.board[r1][c1]
        self.board[r1][c1] = '-'

    def play_random_game(self, max_moves=10000):
        turn = 'white'
        for move_num in range(max_moves):
            moves = self.get_piece_moves(turn)
            if not moves:
                print(f"No moves for {turn}. Game over.")
                break
            move = random.choice(moves)
            self.make_move(move)
            print(f"Move {move_num+1}: {turn} moves {move}")
            self.print_board()
            turn = 'black' if turn == 'white' else 'white'
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # 8x8 board, each cell can be empty or have a piece
        # Uppercase = White, Lowercase = Black
        # R=Rook, N=Knight, B=Bishop, Q=Queen, K=King, P=Pawn
        board = [
            ['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']
        ]
        return board

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

if __name__ == "__main__":
    chess = ChessBoard()
    chess.print_board()
    print("Choose mode:")
    print("1: Human vs AI (You are White)")
    print("2: Human vs Human")
    print("3: AI vs AI")
    mode = input("Enter 1, 2, or 3: ").strip()

    def get_human_move(chess, color):
        while True:
            try:
                move_str = input(f"{color} move (e.g. e2e4): ").strip().lower()
                if len(move_str) != 4:
                    print("Invalid format. Use e2e4.")
                    continue
                cols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
                r1, c1 = 8-int(move_str[1]), cols[move_str[0]]
                r2, c2 = 8-int(move_str[3]), cols[move_str[2]]
                move = ((r1,c1),(r2,c2))
                moves = chess.get_piece_moves(color)
                if move in moves:
                    return move
                else:
                    print("Illegal move. Try again.")
            except Exception:
                print("Invalid input. Try again.")

    if mode == '1':
        turn = 'white'
        for move_num in range(50):
            winner = chess.get_winner()
            if winner:
                print(f"{winner.capitalize()} wins by capturing the king!")
                chess.print_board()
                break
            if turn == 'white':
                moves = chess.get_piece_moves('white')
                if not moves:
                    print("No moves for white. Game over.")
                    break
                move = get_human_move(chess, 'white')
                chess.make_move(move)
            else:
                moves = chess.get_piece_moves('black')
                if not moves:
                    print("No moves for black. Game over.")
                    break
                # Prefer captures if available
                captures = [m for m in moves if chess.board[m[1][0]][m[1][1]] != '-']
                if captures:
                    move = random.choice(captures)
                else:
                    move = random.choice(moves)
                print(f"AI (black) moves {move}")
                chess.make_move(move)
            chess.print_board()
            turn = 'black' if turn == 'white' else 'white'
        else:
            winner = chess.get_winner()
            if winner:
                print(f"{winner.capitalize()} wins by capturing the king!")
            else:
                print("Draw or move limit reached.")
    elif mode == '2':
        turn = 'white'
        for move_num in range(50):
            winner = chess.get_winner()
            if winner:
                print(f"{winner.capitalize()} wins by capturing the king!")
                chess.print_board()
                break
            moves = chess.get_piece_moves(turn)
            if not moves:
                print(f"No moves for {turn}. Game over.")
                break
            move = get_human_move(chess, turn)
            chess.make_move(move)
            chess.print_board()
            turn = 'black' if turn == 'white' else 'white'
        else:
            winner = chess.get_winner()
            if winner:
                print(f"{winner.capitalize()} wins by capturing the king!")
            else:
                print("Draw or move limit reached.")
    else:
        print("Random moves: White vs Black AI")
        turn = 'white'
        for move_num in range(1000):
            import time
            time.sleep(0.8)
            winner = chess.get_winner()
            if winner:
                print(f"{winner.capitalize()} wins by capturing the king!")
                chess.print_board()
                break
            moves = chess.get_piece_moves(turn)
            if not moves:
                print(f"No moves for {turn}. Game over.")
                break
            # Prefer captures if available
            captures = [m for m in moves if chess.board[m[1][0]][m[1][1]] != '-']
            if captures:
                move = random.choice(captures)
            else:
                move = random.choice(moves)
            chess.make_move(move)
            print(f"Move {move_num+1}: {turn} moves {move}")
            chess.print_board()
            turn = 'black' if turn == 'white' else 'white'
        else:
            winner = chess.get_winner()
            if winner:
                print(f"{winner.capitalize()} wins by capturing the king!")
            else:
                print("Draw or move limit reached.")
