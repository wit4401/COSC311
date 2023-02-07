# HW 1.2
def should_play(outlook,humidity,wind):
    retval=True # declare retval with default condition True
    
    if outlook==0: # if outlook sunny
        if humidity: # if humidity is high
            retval=False # return False (set retval)
    
    elif outlook==1: # if outlook is rain 
        if wind: # if wind is strong
            retval=False # return False (set retval)

    return retval # return result of the decision tree

if __name__=="__main__":
    outlook=int(input('Please enter outlook (0 = Sunny, 1 = Rain, 2+ = Overcast):')) # user input for 0 (Sunny), 1 (Rainy), or 2 (Overcast)
    humidity=bool(input('Please enter humidity (0 = High, 1 = Normal):')) # user input for 0 (High) or 1 (Normal)
    wind=bool(input('Please enter wind speed (0 = Strong, 1 = Weak):')) # user input for 0 (Strong) or 1 (Weak)

    # if the function return true: optimal for tennis & if not: not optimal for tennis and tell user
    if should_play(outlook,humidity,wind):
        print('Optimal conditions to play tennis')
    else:
        print('Not optimal conditions to play tennis')