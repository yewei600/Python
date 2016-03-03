def searchRotatedList(List,left,right,x):
    mid=(left+right)/2
    if x==List[mid]:
        return mid
    if right<left:
        return -1
    
    #find which side is normally ordered. 
    if List[left]<List[mid]:    #left is normally ordered
        if x>=List[left] and x<List[mid]:
            return searchRotatedList(List,left,mid-1,x)
        else:
            return searchRotatedList(List,mid+1,right,x);
    
    elif List[mid]<List[left]:  #right is normally ordered
        if x>List[mid] and x<=List[right]:
            return searchRotatedList(List,mid+1,right,x)
        else:
            return searchRotatedList(List,left,mid-1,x)
    
    return -1



theList=[15,16,19,20,1,3,5,7,9,11]

searchRotatedList(theList,0,len(theList)-1,11)
        
