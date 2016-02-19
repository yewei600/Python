from numpy import matrix

A = matrix( [[0,2,3],[11,10,0],[21,22,23]])


def zero_matrix(mat):
    print "the old matrix:"
    print mat
    row=[]
    col =[]
    for i in range(0,mat.shape[0]):
        for j in range(0,mat.shape[1]):
            if mat[i,j]==0:
                row.append(i)
                col.append(j)
    
    for i in row:
        mat[i,:]=0
    for j in col:
        mat[:,j]=0
        
    print "the new matrix:"
    print mat        
   
                

zero_matrix(A)
    
    