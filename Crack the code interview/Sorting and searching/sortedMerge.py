def sortedMerge(A,B):
    print "first array is ",A
    print "second array is ",B
    iA=len(A)-len(B)-1   #index for A
    iB=len(B)-1   #index for B
    k=len(A)-1
    
    print iA,iB,k
    
    while iB>=0:
        if iA>=0 and A[iA]>B[iB]:
            A[k]=A[iA]
            iA-=1
        else:
            A[k]=B[iB]
            iB-=1
        k-=1
                   
    print(A)

s=[1,3,5,7,0,0,0]
t=[2,4,6]

sortedMerge(s,t)       
    
            
    