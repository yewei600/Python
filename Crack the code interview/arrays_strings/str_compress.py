def str_compress(s):
    d={}
    newStr=""
    for char in s:
        if(d.get(char)==None):
            d[char]=1
        else:
            d[char]+=1
    for key in sorted(d.keys()):
        newStr+=str(d[key])
        newStr+=str(key)
    return newStr
        
    
print str_compress("hi")