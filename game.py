import boardcode
import ai
import time
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
def ai_turn(board, aiplayer):
    move = ai.ai_turn(board, aiplayer)
    boardcode.player_move(aiplayer, move[0], move[1], board)
    boardcode.print_board(board)
    return boardcode.new_winning(board)
def check_winner(board):
    winner = boardcode.new_winning(board)
    if winner:
        print(f"{winner} wins")
        return True
    if is_board_full(board):
        print("It's a tie")
        return True
    return False       
def main():
    mode=input("Would you like to play a friend or AI: ").lower()
    while mode not in ['ai', 'p']:
        mode = input("Play against friend (p) or AI (ai)? ").lower()
    if (mode=='ai'):
        heads=input("Would you like to go first? y/n")
        if (heads=='n'):
            freshboard = [row[:] for row in boardcode.board]
            #boardcode.print_board(freshboard)
            player='X'
            aiplayer='O'
            winner=boardcode.new_winning(freshboard)
            while winner==None:
                #ai_turn(freshboard,aiplayer)
                print("AI TURN")
                time.sleep(0.2)
                winner = ai_turn(freshboard, aiplayer)
                if winner:
                    print(f"{winner} wins")
                    break
                if is_board_full(freshboard):
                    print("It's a tie")
                    break

                # Players Turn
                print("Player Turn")
                player_turn(player,freshboard)
                winner=boardcode.new_winning(freshboard)
                if winner:
                    print(f"{winner} wins")
                    break
                if is_board_full(freshboard) :
                    print("It's a tie")
                    break
        if(heads=='y'):
            freshboard = [row[:] for row in boardcode.board]
            #boardcode.print_board(freshboard)
            player='X'
            aiplayer='O'
            winner=boardcode.new_winning(freshboard)
            while winner==None:
                # Players Turn
                print("Player Turn")
                player_turn(player,freshboard)
                winner=boardcode.new_winning(freshboard)
                if winner:
                    print(f"You :{winner}  wins")
                    break
                if is_board_full(freshboard) :
                    print("It's a tie")
                    break
                #ai_turn(freshboard,aiplayer)
                print("AI TURN")
                time.sleep(0.2)
                winner = ai_turn(freshboard, aiplayer)
                if winner:
                    print(f"{winner} wins")
                    break
                if is_board_full(freshboard):
                    print("It's a tie")
                    break
    if(mode=='p'):
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
    