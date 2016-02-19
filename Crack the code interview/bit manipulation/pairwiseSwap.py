def pairwiseSwap(num):
#swap odd and even bits in an integer with as few instructions as possible
    tmp=0
    num=bin(num)
    num=num[2:]
    num=list(num)
    if len(num)%2:
        num.insert(0,'0')
    print("before swapping: "),
    print num
    
    for i in range(0,len(num),2):
        tmp=num[i]
        num[i]=num[i+1]
        num[i+1]=tmp

    print(" after swapping: "),
    print num
        
        
        
        
        
    