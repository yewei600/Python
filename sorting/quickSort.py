import random

def quickSort(aList):
    less = []
    pivotList = []
    more = []
    if len(aList) <= 1:
        return aList
    else:
        pivot = aList[0]
        for i in aList:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more


a=[]

for i in range(1,10):
    a.append(random.randint(1,20))

print "Before sorting: "
print a

print "After sorting: "
a = quickSort(a)
print a


