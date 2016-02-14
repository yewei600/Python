def lessThan4 (aList):
    answer = []
    for i in range (0,len(aList)):
        if len(aList[i])<4:
            answer.append(aList[i])
    
    return answer
            