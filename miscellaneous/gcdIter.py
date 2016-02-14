def gcdIter(a, b):
    test = min(a,b)
    while test>=1:
        if a%test==0 and b%test==0:
            break
        test-=1
    
    return test