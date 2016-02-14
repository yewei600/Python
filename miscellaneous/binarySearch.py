import random

def bisectionSearch (lowerBound,upperBound):
    target = random.randint(lowerBound,upperBound)
    bottom = lowerBound
    top = upperBound
    guess = (top-bottom)/2+1
    
    print "your guess is %d" % int(guess)
    
    while guess != target:
        if guess < target:
            bottom = guess
            guess = (top-bottom)/2+1
            print "guess too small. Now bottom is %d, top is %d" % (bottom, top)
        elif guess > target:
            top = guess
            guess = (top-bottom)/2+1
            print "guess too big. Now bottom is %d, top is %d" % (bottom, top)

        
    print "The random number is %d" % guess
            
            
            
         
        
    
    
    