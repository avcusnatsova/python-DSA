import math

def selectionsort(customlist):
    for i in range(len(customlist)):
        minindex = i
        for j in range(i+1, len(customlist)):
            if customlist[minindex] > customlist[j]:
                minindex = j
        customlist[i], customlist[minindex] = customlist[minindex], customlist[i]
    print(customlist)
cList = [2,1,7,6,5,3,4,9,8]
print(cList)
selectionsort(cList)