def mergesort(arr):
    if len(arr) <= 1:
        return arr
    

    mid = len(arr) // 2
    left_arr = mergesort(arr[:mid])
    right_arr = mergesort(arr[mid:])

    i = j = k = 0

    merged = [0] * (len(left_arr) + len(right_arr))

    while i < len(left_arr)  and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merged[k] = left_arr[i]
            i+=1
        else:
            merged[k] = right_arr[j]
            j+=1
        k += 1
    while i < len(left_arr):
        merged[k] = left_arr[i]
        i+=1
        k+=1
    while j < len(right_arr):
        merged[k] = right_arr[j]
        j+= 1
        k+=1
    return merged
arr1 = [45,23,54,12,90,78]
print(mergesort(arr1))

