#!/usr/bin/python3.5

import numpy as np

#white = 1
#black = -1
#king = 10

def move(board):

    winner = 0

    #move logic

    if( 10 not in board):
        winner = -1

    if( 10 in ( board[0] or board[8] ) ):
        winner = 1
    for row in board:
        if( row[0] == 10 or row[8] == 10 ):
            winner = 1



def calc_move( (x,y), board ):
    valid = np.ones_like(board)
    x = x
    y = y
    #check spots above piece
    if(x>0):
        if (board[x-1,y] == 1 or board[x-1,y] == 10 ):
            valid[x-1,y] = 0
            while(x>=1):
                valid[x-1,y] = 0
                x = x-1
        else:
            x = x-1

    #check spots below piece
    if(x<8):
        if (board[x+1,y] == 1 or board[x+1,y] == 10 ):
            valid[x+1,y] = 0
            while(x>=1):
                valid[x+1,y] = 0
                x = x+1
        else:
            x = x+1

    #check spots left of piece
    if(y>0):
        if (board[x,y-1] == 1 or board[x,y-1] == 10 ):
            valid[x,y-1] = 0
            while(y>=1):
                valid[x,y-1] = 0
                y = y - 1
        else:
            y = y - 1

    #check spots below piece
    if(y<8):
        if (board[x,y+1] == 1 or board[x,y+1] == 10 ):
            valid[x,y+1] = 0
            while(x>=1):
                valid[x,y+1] = 0
                y = y+1
        else:
            y = y+1

    return(valid)

if __name__ == "__main__":
    board = [[0,0,0,-1,-1,-1,0,0,0],
             [0,0,0,0,-1,0,0,0,0],
             [0,0,0,0,1,0,0,0,0],
             [-1,0,0,0,1,0,0,0,-1],
             [-1,-1,1,1,10,1,1,-1,-1],
             [-1,0,0,0,1,0,0,0,-1],
             [0,0,0,0,1,0,0,0,0],
             [0,0,0,0,-1,0,0,0,0],
             [0,0,0,-1,-1,-1,0,0,0]]

    winner = 0

    while(winner == 0):
        board,winner = move(board)
        print(board)

#black "Scoring"
#reduce number of moves made by white use as criteria
#maximize # of moves in made by black as criteria
