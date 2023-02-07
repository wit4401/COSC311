# HW 1.4
from random import randint # import randint from random

totals=[0 for i in range(11)] # list will stores the total number of times a sum is rolled
n=int(input("Enter number of simulations: ")) # user input for the number of simulations

# Loop runs until the proper number of simulations have been ran
for i in range(n):
    die1=randint(1,6) # generate outcome for die 1
    die2=randint(1,6) # generate outcome for die 2
    totals[die1+die2-2]+=1 # adds to the proper total in the list

i=2 # an iterator for a user friendly output

# Loop to print all the probabilities of possible sums ( total_rolled/total_sims * 100% )
for val in totals:
    print('probability of rolling {}: {:3.2f}%'.format(i,float(val/n)*100))
    i+=1 # increment in the iterator
