def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup=()
    for i in range (0,len(aTup)):
        if i%2 == 0:
            newTup = newTup + (aTup[i],)
    
    return newTup
