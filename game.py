import boardcode
import ai
def is_board_full(board):
    a=[row for columns in board for row in columns]
    return '-' not in a
def player_turn(player,board):
    while True:
        try:
            x = int(input("X Coordinate (0-2): "))
            y = int(input("Y Coordinate (0-2): "))
        except ValueError:
            print("Please enter valid integers between 0 and 2")
            continue

        if x not in range(3) or y not in range(3):
            print("Coordinates must be 0, 1, or 2")
            continue

        if boardcode.player_move(player, x, y, board):
            boardcode.print_board(board)
            break

def main():
    #freshboard=boardcode.board.copy() Shallow Copy
    freshboard = [row[:] for row in boardcode.board]
    boardcode.print_board(freshboard)
    player1='X'
    player2='O'
    while True:
        #print(f"free coordinates {ai.get_empty_cells(freshboard)}")# get empty cells
        player_turn(player1,freshboard)
        winner=boardcode.new_winning(freshboard)
        if winner:
            print(f"{winner} wins")
            break
        if is_board_full(freshboard) :
            print("It's a tie")
            break

        player_turn(player2,freshboard) 
        winner=boardcode.new_winning(freshboard)
        if winner:
            print(f"{winner} wins")
            break
        if is_board_full(freshboard) :
            print("It's a tie")
            break
if __name__ == "__main__":
    main() 
    