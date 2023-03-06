"""
Homework 2: Tic-Tac-Toe
A two player text version of Tic-Tac-Toe.
"""

# display tic tac toe board
def display_grid(board):
    row = 0
    for i in range(9):
        if (i+1)%3!=0:
            print(board[row][i%3],end='')
            print('|',end='')
        else:
            print(board[row][i%3])
            if i!=8:
                print('-'*5)
            row+=1

# check if there is a winner
def check_winner(board):
    win=False
    if board[0][0]==board[0][1] and board[0][1]==board[0][2]:
        if board[0][0]!=' ': 
            win=True
    elif board[1][0]==board[1][1] and board[1][1]==board[1][2]:
        if board[1][0]!=' ':
            win=True
    elif board[2][0]==board[2][1] and board[2][1]==board[2][2]:
        if board[2][0]!=' ':
            win=True
    elif board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0]!=' ':
            win=True
    elif board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        if board[0][2]!=' ':
            win=True
    return win

# checks for a tied game 'i.e. the board is full'
def check_tie(board):
    tie=True
    for row in board:
        for val in row:
            if val==' ':
                tie=False
    return tie

# main of the program         
if __name__=="__main__":
    game_grid = [[' ',' ',' '],
                 [' ',' ',' '],
                 [' ',' ',' ']]
    player = 'X'
    flag=True
    
    print("Game Begin!\n")
    display_grid(game_grid)
    while flag:
        print('\n'+player+"'s turn.")
        row=col=-1
        row=int(input("Row to place (0-2):"))
        col=int(input("Column to place (0-2):"))
        if (row<0 and row>2) or (col<0 and col>2) or game_grid[row][col]!=' ':
            print("\nInvalid Move!")
        else:
            game_grid[row][col]=player
            win=check_winner(game_grid)
            tie=check_tie(game_grid)
            
            print()
            display_grid(game_grid)

            if win:
                print("\nWinner is " + player + "!")
                flag=False
            elif tie:
                print("\nIt's a tie!")
                flag=False
            
            if player=='X':
                player='O'
            else:
                player='X'
