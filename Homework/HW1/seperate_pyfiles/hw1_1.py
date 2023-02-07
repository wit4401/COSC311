# HW 1.1
oddSum=0 # define oddSum variable
evenSum=0 # define evenSum variable
currValue=1 # define currValue variable with the first in the sequence

# Loops until it reach the 20th value in the arithmetic sequence
for i in range(2,22):
    print(currValue,'->',end=" ") # prints out the current number in the sequence
    
    # if current value is even: adds to the even sum | if not: adds to the odd sum
    if currValue%2==0:
        evenSum+=currValue
    else:
        oddSum+=currValue
        
    currValue+=i # gets the next sum in the arithmetic sequence a_n+1 = a_n + (n+2) ( n = 0, 1, 2,... ) (hence i starting at 2)

# print out the resulting sums from the sequence as defined in the problem
print('\nOdd Value Sum:',oddSum)
print('Even Value Sum:',evenSum)