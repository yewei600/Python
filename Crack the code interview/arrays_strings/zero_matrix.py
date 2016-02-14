def zero_matrix(mat):
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
        
             
   
                
    
    
    