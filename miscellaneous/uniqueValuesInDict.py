def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    dictValues = aDict.values()
    dictKeys = aDict.keys()
    dupValues=[]
    uniqueKeys = []
    
    # list of duplicate values
    for item in dictValues:
        if dictValues.count(item)>1:
            dupValues.append(item)
    
    
    for item in dictKeys:
        if aDict[item] not in dupValues:
            uniqueKeys.append(item)
    
    return sorted(uniqueKeys)