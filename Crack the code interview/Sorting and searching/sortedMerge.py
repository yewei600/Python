def sortedMerge(A,B):
    print "A is ",A
    print "B is ",B
    dif=len(A)-len(B)
    i=len(A)-dif
    j=len(B)
    
    while i>=0 and j>=0:
        if A[i-1]>B[i-1]:
            A[i-1+dif]=A[i-1]
            i=i-1
        else:
            A[i-1+dif]=A[i-1]
            j=j-1
        
    print(A)        
    
            
    