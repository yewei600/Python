def recurPowerNew(base, exp):
    if exp==0:
        return 1
    elif exp%2==0:
        return recurPowerNew(base*base,exp/2)
    elif exp%2!=0:
        return recurPowerNew(base,exp-1)