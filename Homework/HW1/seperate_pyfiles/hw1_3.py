# HW 1.3
def draw_octagon(L):
    # instructions for the top portion of the octagon (L-1) lines increasing by 2 '*' each line
    for i in range(L-1,0,-1):
        # for loop for white space starting with L-1 spaces and decreasing by 1
        for j in range(0,i):
            print(' ',end="")
        # for loop for the '*' characters starting with L and increasing to L+(L-1)*2
        for j in range(0,(L-1-i)*2+L):
            print('*',end="")
        print()
    
    # instructions for the middle of the octagon a rectangle ( L x (2x(L-1)+L) )
    for i in range(0,L):
        # print the line of '*' with (2x(L-1)+L) of them
        for j in range(0,2*(L-1)+L):
            print('*',end="")
        print()
    
    # instructions for the bottom portion of the octagon (L-1) lines decreasing by two '*' each line
    # essentially it is the reverse of the top portion
    for i in range(1,L):
        for j in range(i,0,-1):
            print(' ',end="")
        for j in range((L-1-i)*2+L,0,-1):
            print('*',end="")
        print()

# just some proper python syntax when defining functions for some flair
if __name__=="__main__":
    L = -1
    # Loop that checks for the proper length
    while L < 2:
        L = int(input('Enter length of the octagon (L>1): '))
        
        # L is less than 2 print invalid input and repeats with another user input
        if L<2: 
            print('Invalid Input')

    draw_octagon(L) # calls the function