def URLify(str):
    newStr = ""
    for char in str:
        if char ==' ':
            newStr+='%20'
        else:
            newStr+=char
    return newStr
        
