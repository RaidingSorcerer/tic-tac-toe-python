import boardcode
import game
import random

def get_empty_cells(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                empty.append((i, j))
    return empty

def ai_turn(board,move):
    if(move=='X'):
        opponent='O'
    else:
        opponent='X'
    corners = [(0,0), (0,2), (2,0), (2,2)]
    available=get_empty_cells(board)
    #Check for winning moves
    for combo in available:
        board[combo[0]][combo[1]]=move
        if(boardcode.new_winning(board)== move):
            return combo
        else:
            board[combo[0]][combo[1]] = '-'
    #Blcoking Opponent
    for combo in available:
        board[combo[0]][combo[1]]=opponent
        if(boardcode.new_winning(board)==opponent):
            board[combo[0]][combo[1]] = '-'
            return combo
        else:
            board[combo[0]][combo[1]] = '-'
    corner=[(x,y) for (x,y) in corners if (x,y) in available]
    if corner:
        return random.choice(corner)
    #Pick a center
    if (1,1) in available:
            return(1,1)
    return random.choice(available)


    


'''
#print(get_empty_cells(board))
print(ai_turn(board,'o'))
boardcode.print_board(board)
print("John doe")
board=[ 
       ['x','o','o'],
       ['o','-','o'],
       ['o','o','o']
]
'''
