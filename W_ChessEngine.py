class ChessPiece:  # parent class for chess pieces
    def __init__(self, color):
        self.color = color
        self.has_moved = False

class Pawn(ChessPiece):
    def __str__(self):
        return 'P' if self.color == 'white' else 'p'

    def valid_moves(self, board, row, col):
        moves = []
        direction = 1 if self.color == 'white' else -1

        # forward move
        if 0 <= row + direction < 8 and board[row + direction][col] is None:
            moves.append((row + direction, col))

            # initial two-step move
            if (self.color == 'white' and row == 1) or (self.color == 'black' and row == 6):
                if board[row + 2 * direction][col] is None:
                    moves.append((row + 2 * direction, col))

        # capturing pieces diagonally
        for c in [-1, 1]:
            if 0 <= row + direction < 8 and 0 <= col + c < 8:
                if board[row + direction][col + c] and board[row + direction][col + c].color != self.color:
                    moves.append((row + direction, col + c))
        return moves

class Rook(ChessPiece):
    def __str__(self):
        return 'R' if self.color == 'white' else 'r'

    def valid_moves(self, board, row, col):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            for i in range(1, 8):
                r, c = row + i * dr, col + i * dc
                if 0 <= r < 8 and 0 <= c < 8:
                    if board[r][c] is None:
                        moves.append((r, c))
                    elif board[r][c].color != self.color:
                        moves.append((r, c))
                        break
                    else:
                        break
                else:
                    break

        return moves

class Knight(ChessPiece):
    def __str__(self):
        return 'N' if self.color == 'white' else 'n'

    def valid_moves(self, board, row, col):
        moves = []
        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]

        for dr, dc in knight_moves:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None or board[r][c].color != self.color:
                    moves.append((r, c))

        return moves

class Bishop(ChessPiece):
    def __str__(self):
        return 'B' if self.color == 'white' else 'b'

    def valid_moves(self, board, row, col):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            for i in range(1, 8):
                r, c = row + i * dr, col + i * dc
                if 0 <= r < 8 and 0 <= c < 8:
                    if board[r][c] is None:
                        moves.append((r, c))
                    elif board[r][c].color != self.color:
                        moves.append((r, c))
                        break
                    else:
                        break
                else:
                    break

        return moves

class Queen(ChessPiece):
    def __str__(self):
        return 'Q' if self.color == 'white' else 'q'

    def valid_moves(self, board, row, col):
        moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for dr, dc in directions:
            for i in range(1, 8):
                r, c = row + i * dr, col + i * dc
                if 0 <= r < 8 and 0 <= c < 8:
                    if board[r][c] is None:
                        moves.append((r, c))
                    elif board[r][c].color != self.color:
                        moves.append((r, c))
                        break
                    else:
                        break
                else:
                    break

        return moves

class King(ChessPiece):
    def __str__(self):
        return 'K' if self.color == 'white' else 'k'

    def valid_moves(self, board, row, col):
        moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None or board[r][c].color != self.color:
                    moves.append((r, c))

        return moves

# Update the evaluate function to work with the python-chess Board object
def evaluate(board):
    # Piece values
    piece_values = {
        chess.PAWN: 1,
        chess.ROOK: 5,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.QUEEN: 9,
        chess.KING: 0
    }

    # Evaluate white and black pieces
    wp, wr, wn, wb, wq, wk = 0, 0, 0, 0, 0, 0
    bp, br, bn, bb, bq, bk = 0, 0, 0, 0, 0, 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = piece_values.get(piece.piece_type, 0)
            if piece.color == chess.WHITE:
                if piece.piece_type == chess.PAWN:
                    wp += value
                elif piece.piece_type == chess.ROOK:
                    wr += value
                elif piece.piece_type == chess.KNIGHT:
                    wn += value
                elif piece.piece_type == chess.BISHOP:
                    wb += value
                elif piece.piece_type == chess.QUEEN:
                    wq += value
                elif piece.piece_type == chess.KING:
                    wk += value
            else:
                if piece.piece_type == chess.PAWN:
                    bp += value
                elif piece.piece_type == chess.ROOK:
                    br += value
                elif piece.piece_type == chess.KNIGHT:
                    bn += value
                elif piece.piece_type == chess.BISHOP:
                    bb += value
                elif piece.piece_type == chess.QUEEN:
                    bq += value
                elif piece.piece_type == chess.KING:
                    bk += value

    # Total evaluation
    return (wp + wr + wn + wb + wq + wk) - (bp + br + bn + bb + bq + bk)

####Board Evaluation
PAWN_TABLE = [
    0,  0,  0,  0,  0,  0,  0,  0, 
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5,  5, 10, 25, 25, 10,  5,  5, 
    0,  0,  0, 20, 20,  0,  0,  0, 
    5, -5,-10,  0,  0,-10, -5,  5, 
    5, 10, 10,-20,-20, 10, 10,  5, 
    0,  0,  0,  0,  0,  0,  0,  0
]
KNIGHTS_TABLE = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50
]
BISHOPS_TABLE = [
    -20,-10,-10,-10,-10,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5, 10, 10,  5,  0,-10,
    -10,  5,  5, 10, 10,  5,  5,-10,
    -10,  0, 10, 10, 10, 10,  0,-10,
    -10, 10, 10, 10, 10, 10, 10,-10,
    -10,  5,  0,  0,  0,  0,  5,-10,
    -20,-10,-10,-10,-10,-10,-10,-20
]
ROOKS_TABLE = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10, 10, 10, 10, 10,  5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    0,  0,  0,  5,  5,  0,  0,  0
]
QUEENS_TABLE = [
    -20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5,  5,  5,  5,  0,-10,
    -5,  0,  5,  5,  5,  5,  0, -5,
    0,  0,  5,  5,  5,  5,  0, -5,
    -10,  5,  5,  5,  5,  5,  0,-10,
    -10,  0,  5,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20
]
KINGS_TABLE = [
    -50,-40,-30,-20,-20,-30,-40,-50,
    -30,-20,-10,  0,  0,-10,-20,-30,
    -30,-10, 20, 30, 30, 20,-10,-30,
    -30,-10, 30, 40, 40, 30,-10,-30,
    -30,-10, 30, 40, 40, 30,-10,-30,
    -30,-10, 20, 30, 30, 20,-10,-30,
    -30,-30,  0,  0,  0,  0,-30,-30,
    -50,-30,-30,-30,-30,-30,-30,-50
]

import chess
def _determine_best_move(board, is_white, depth = 3):

    best_move = -100000 if is_white else 100000
    best_final = None
    for move in board.legal_moves:
        board.push(move)
        value = _minimax_helper(depth - 1, board, -10000, 10000, not is_white)
        board.pop()
        if (is_white and value > best_move) or (not is_white and value < best_move):
            best_move = value
            best_final = move
    return best_final

def _minimax_helper(depth, board, alpha, beta, is_maximizing):
    if depth <= 0 or board.is_game_over():
        return evaluate(board)

    if is_maximizing:
        best_move = -100000
        for move in board.legal_moves:
            board.push(move)
            value = _minimax_helper(depth - 1, board, alpha, beta, False)
            board.pop()
            best_move = max(best_move, value)
            alpha = max(alpha, best_move)
            if beta <= alpha:
                break
        return best_move
    else:
        best_move = 100000
        for move in board.legal_moves:
            board.push(move)
            value = _minimax_helper(depth - 1, board, alpha, beta, True)
            board.pop()
            best_move = min(best_move, value)
            beta = min(beta, best_move)
            if beta <= alpha:
                break
        return best_move

if __name__ == '__main__':
    board = chess.Board()
    is_white = input( 'white (d) or black (u) : ' ).lower()[0] == "w"

    print()
    print( f'Chess Board' )
    print(board)

    if is_white:
        while not board.is_game_over():
            print()
            while True:
                try:
                    move = board.parse_san(input('Enter your move (ex: e2e4): '))
                except ValueError:
                    print(f'That is not a valid move!')
                    continue
                break
            board.push(move)

            move = _determine_best_move(board, False)
            board.push(move)

            print()
            print(f'Black made the move: {move}' )
            print()
            print(f'= Board State =')
            print(board)
            print()
    else:
        while not board.is_game_over():
            move = _determine_best_move(board, True)
            board.push(move)

            print()
            print( f'White made the move: {move}' )
            print()
            print(f'= Board State =')
            print(board)
            print()
            while True:
                try:
                    move = board.parse_san(input( 'Enter your move: '))
                except ValueError:
                    print(f'That is not a valid move!' )
                    continue
                break
            board.push(move)

    print(f'Game over' )



