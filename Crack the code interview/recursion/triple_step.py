'''
--top down approach, the very last hop child made?
--if knew number of paths to each of the steps before step 100,could we computer
the number of steps to 100?
--compute num of steps to 100 by num of steps to 99, 98, 97    do this then this
--f(100)=f(99)+f(98)+f(97)
-- try memorization

'''

def triple_step(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    
    return triple_step(n-1)+triple_step(n-2)+triple_step(n-3)
    

def triple_step2(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
       return triple_step(n-1)+triple_step(n-2)+triple_step(n-3)
        
    