def linearsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
a = [23,45,67,89,10,20]
print(linearsearch(a, 89))