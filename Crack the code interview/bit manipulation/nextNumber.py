def nextNumber(num):
    #find the next smallest and next largest number with same amount of 0s and
    #1s in their binary representation
    '''
    flip 1-0 or 0-1, number get bigger if 0->1 bit is more significant than 1->0 bit
    
    '''

    changed1=False
    changed0=False

    binNum=bin(num)
    binNum=binNum[2:]
    binNum=list(binNum)
    if '0' not in binNum:
        binNum.insert(0,'0')
        print ("0th place number is %s")%binNum[0]
          
    print binNum
    print "length of binNUm is %d" %len(binNum)
   
   
    nextSmall=binNum[:] #the next smallest: find the first 10 pair and swap to 01
    #first 0,  first 1 after the first 0
    
    nextLarge=binNum[:] #the next largest: find the first 01 pair and swap to 10
    #first 1, first 0 after the first 1
      
    
    #find the first 10 pair
    for i in range(len(binNum),0,-1):
        if nextSmall[i-1]=='0'and changed0==False:
            nextSmall[i-1]='1'
            changed0=True
            continue
        elif nextSmall[i-1]=='1' and changed0:
            nextSmall[i-1]='0'
            print "the next smallest is",
            print nextSmall
        
    #find the first 01 pair

    print
    for i in range(len(binNum),0,-1):
        print i,
        print nextLarge[i-1]
        print changed1
        if nextLarge[i-1]=='1'and changed1==False:
            nextLarge[i-1]='0'
            changed1=True
            print "NIGGA is at %d" %i
            continue
        elif nextLarge[i-1]=='0'and changed1:
            print "I'm HERE!!!"
            nextLarge[i-1]='1'
            print "the next largest is",
            print "2nd Nigga"
            print nextLarge
            