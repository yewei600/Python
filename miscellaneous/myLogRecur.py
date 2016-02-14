def myLogRecur(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if x<b:
        return 0
    return 1+myLogRecur(x/b,b)