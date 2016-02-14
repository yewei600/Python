def sumDigitsRecur(N):
    '''
    N: a non-negative integer
    '''
    if N/10==0:
        return N
    return N%10+ sumDigitsRecur(N/10)
        