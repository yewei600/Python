def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L)==0:
        return float('NaN')
    totLength =0
    sigma=0
    for string in L:
        totLength+=len(string)
    mean=totLength/float(len(L))
    
    for string in L:
        sigma+=(len(string)-mean)**2
    
    return (sigma/float(len(L)))**0.5
    
        
    
        