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
    print("\t   0   1   2")
    print("\t  -----------")
    counter=0
    for column in board:
        print(f"\t{counter}|",end=' ')
        for row in column:
            print(f"{row}  ",end=' ')
        print()
        counter+=1


def new_winning(board):
    winners=[[(0,0),(0,1),(0,2)],
         [(1,0),(1,1),(1,2)],#ROWS
         [(2,0),(2,1),(2,2)],

         [(0,0),(1,0),(2,0)],
         [(0,1),(1,1),(2,1)],# COLUMNS
         [(0,2),(1,2),(2,2)],

         [(0,0),(1,1),(2,2)],#DIAGONALS
         [(0,2),(1,1),(2,0)]
         ]
    for combo in winners:
        checklist=[board[cell[0]][cell[1]] for cell in combo  ]
        if(checklist[0]==checklist[1]==checklist[2] and checklist[0]!='-'):
            return checklist[0]
    