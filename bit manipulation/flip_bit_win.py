def flip_bit_win(num):
    #store each sequence of ones in array.
    seq = []
    cnt = 0
    bnd =0
    end =0
    largest =0
    for i in range(0,len(num)):
        if num[i]=='0':
            #the first ever 0
            if bnd==0:
                bnd=1
            #2nd zero
            elif bnd==1:
                bnd=2
                seq.append(cnt)
                cnt=0
                bnd=1
        if num[i]=='1':
            if(i==0):
                bnd=1            
            cnt+=1
            if(i==len(num)-1):
                seq.append(cnt)

    for i in range(0,len(seq)):
        if i<len(seq)-1:
            if seq[i]+seq[i+1]>largest:
                largest = seq[i]+seq[i+1]
    
    print(largest+1)
                

                
                
            
                

            



    
        


        

            
        
    
        
    
    
    
    