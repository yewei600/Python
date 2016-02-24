def binarySearch(theList,num):
    theList=sorted(theList)
    low=0
    high=len(theList)-1
    
    while(low<=high):
        mid=(low+high)/2
        if theList[mid]<num:   #mid element < searchNum
            low=mid+1
        elif theList[mid]>num:   #mid element > searchNum
            high=mid-1
        else:
            return True
   
    return False
        

def binarySearchRecursive(theList,num,low,high):
    if low>high:
        return False
    mid = (low+high)/2
                
            