def conversion(a,b):
    a=bin(a)  
    a=a[2:]
    b=bin(b)  
    b=b[2:]
    cnt=0
    
    digitDiff = abs(len(a)-len(b))
    

    if len(a)<len(b):
         a='0'*digitDiff+a
    else:
        b='0'*digitDiff+b
        
    #check digit difference
    for i in range(0,len(a)):
        if a[i]!=b[i]:
            cnt+=1
    
    return cnt

    
    

    