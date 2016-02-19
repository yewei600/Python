def str_rotation(s,t):
#find if s2 is a rotation of s1 using only one call to isSubstring
    for i in range (0,len(s)):
        if(s[0]==t[i]):
            break;

    firstPart=t[:i]
    tmp=t
    tmp=tmp+firstPart
      
    if s in tmp:
        print t,"is a rotation of",s
    else:          
        print t,"is not a rotation of",s
        
    
    
    