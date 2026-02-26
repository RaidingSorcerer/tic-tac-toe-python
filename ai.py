import boardcode
import game
def get_empty_cells(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                empty.append((i, j))
    return empty
