# 3 types of edits:
#insert,remove,replace (character)

def one_away(s,t):
    if s==t:
        print True
    elif abs(len(s)-len(t))==1:
        if len(s)<len(t):
            return s in t
        else:
            return t in s
    elif len(s)==len(t):
        dif=0
        for i in range(0,len(s)):
            if s[i]!=t[i]:
                dif=dif+1
        if dif==1:
            print True
        else:
            print False
    else:
        return False    
    
    