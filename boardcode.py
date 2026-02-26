board=[ 
       ['-','-','-'],
       ['-','-','-'],
       ['-','-','-']
]

def player_move(player,x,y,board):
    if(board[x][y]== '-'):
        board[x][y]=player
        return True
    else:
        print("Already filled retry")
        return False
        
       


def print_board(board):
    counter=0
    for column in board:
        print(f"\t{counter}",end=' ')
        for row in column:
            print(f"\t{row}",end=' ')
        print()
        counter+=1

def winning(board):
    #Rows
    if board[0][0]== board[0][1]==board[0][2] and board[0][0] !='-':
        return board[0][0]
        
    elif board[1][0]== board[1][1]==board[1][2] and board[1][0] !='-':
        return board[1][0]
        
    elif board[2][0]== board[2][1]==board[2][2] and board[2][0] != '-':
        return board[2][0]
        
    #Columns
    elif board[0][0]== board[1][0]==board[2][0] and board[0][0] !='-':
        return board[0][0]
        
    elif board[0][1]== board[1][1]==board[2][1]and board[0][1] !='-':
        return board[0][1]
        
    elif board[0][2]== board[1][2]==board[2][2]and board[0][2] !='-':
        return board[0][2]
       
    #Diagonals
    elif board[0][0]== board[1][1]==board[2][2] and board[0][0] !='-':
        return board[0][0]
        
    elif board[0][2]== board[1][1]==board[2][0]and board[0][2] !='-':
        return board[0][2]