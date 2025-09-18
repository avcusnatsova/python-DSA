def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i+= 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i] , arr[j] = arr[j] , arr[i]
def quicksort(arr, low,high):
    if low<high:
        p = hoare_partition(arr, low,high)
        quicksort(arr, low, p)
        quicksort(arr, p+1, high)

arr = [90,78,56,43,23,12]
quicksort(arr, 0, len(arr) - 1)
print(arr)