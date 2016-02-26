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
        


#list must be PRESORTED                
def binarySearchRecursive(theList, num,low,high):
	if (high < low):
            return False
	
        mid = low + ((high - low) / 2)
        if theList[mid] > num:
            return binarySearchRecursive(theList, num, low, mid-1)
        elif theList[mid] < num:
            return binarySearchRecursive(theList, num, mid+1, high)
        else:
            return True            