def palindrome_perm(str):
#check if string is a permutation of a palidrome
    d = {}
    unique=0  #for str len of odd number
   
    for char in str:
        if char==' ':
            continue
        if (d.has_key(char)):
            d[char]=d.get(char)+1            
        else:
            d[char]=1
                
    
    for key in d.keys():
        if d[key]==1:
           unique=unique+1
           continue
        elif d[key]%2:
            return False
       
    if unique>1:
        return False
    else:
        return True
    
    
    

            
                
        


        