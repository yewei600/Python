def f(s):
    return 'a' in s


def satisfiesF(L):
    Lcopy = L[:]
    for i in range(len(Lcopy)):
        if f(Lcopy[i])==False:
            L.remove(Lcopy[i])
        
    return len(L)
    
            