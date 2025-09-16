import math

def bubblesort(customlist):
    for i in range(len(customlist) - 1):
        for j in range(len(customlist)-i-1):
            if customlist[j] > customlist[j +1]:
                customlist[j], customlist[j+1] = customlist[j+1], customlist[j]
    print(customlist)
cList = [2,1,7,6,5,3,4,9,8]
print(cList)
bubblesort(cList)
