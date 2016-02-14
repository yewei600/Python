def keysWithValue(aDict,target):
    answer = []
    for key in aDict:
        if aDict[key]==target:
            answer.append(key)
    
    answer.sort()
    return answer
            