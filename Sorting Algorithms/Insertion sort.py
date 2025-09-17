def selectionsort(arr):
    for i in range(len(arr)):
        minindex = i
        for j in range(i+1, len(arr)):
            if arr[minindex] > arr[j]:
                minindex = j
        arr[minindex], arr[i] = arr[i], arr[minindex]
    return arr
clist = [65,45,35,25,15,85,95,75,105]
print(clist)
print(selectionsort(clist))