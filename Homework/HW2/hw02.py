"""
Homework 2: Tic-Tac-Toe
A two player text version of the popular Tic-Tac-Toe.
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
    novar=' '

    # checks the rows
    for row in board:
        if row==['X','X','X'] or row==['O','O','O']:
            win=True
    
    # checks the columns
    for col in range(3):
        if (board[0][col]==board[1][col] and board[1][col]==board[2][col]) and board[0][col]!=' ':
            win=True
    
    # check the diagonals
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!=' ':
        win=True
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]!=' ':
        win=True
    
    return win

# checks for a tied game 'i.e. the board is full'
def check_tie(board):
    tie=True
    for row in board:
        for val in row:
            if val==' ':
                tie=False
                break
        if not tie:
            break
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

        # Error checking for the initial input
        try:
            row=int(input("Row to place (0-2):"))
            col=int(input("Column to place (0-2):"))
        except ValueError: # error catching for string/char inputs
            print('\nPlease Input a Number!')
            continue
        except KeyboardInterrupt: # keyboard interrupts declares no winner & exits program
            import sys
            print("\nNo Winner. Exited Sucessfully.")
            sys.exit()
            
        try: # checks for out of range numbers
            if game_grid[row][col]!=' ': # if space is occupied (not a ' ') the put invalid input and skips back to the start of loop
                print("\nInvalid Input! (Space Occupied)")
                continue
        except IndexError: # if row or col not in range declares invalid move, ignores rest of code, and skips back to the start of the loop
            print("\nInvalid Input! (Row 0-2 & Col 0-2)")
            continue

        # checks if given numbers are negative if so invalid move and skips back to start of loop 
        if row<0 or col<0:
            print("\nInvalid Input!")
            continue
        
        # after all error checking if inputs are valid and in range code executes as normal
        game_grid[row][col]=player

        win=check_winner(game_grid)
        tie=check_tie(game_grid)
        
        print()
        display_grid(game_grid)

        # checks for winner or a tie
        if win:
            print("\nWinner is " + player + "!")
            flag=False
        elif tie:
            print("\nIt's a tie!")
            flag=False
        
        # switches current player turn
        if player=='X':
            player='O'
        else:
            player='X'