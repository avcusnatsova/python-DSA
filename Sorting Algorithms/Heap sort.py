def heapify(cl, n,i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and cl[l] < cl[smallest]:
        smallest = l
    if r<n and cl[r] < cl[smallest]:
        smallest = r
    if smallest != i:
        cl[i], cl[smallest] = cl[smallest], cl[i]
        heapify(cl,n,smallest)
def heapsort(arr):
    n = len(arr)
    for i in range(int(n/2)-1, -1,-1):
        heapify(arr,n,i)
    for i in range(n-1, 0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
nums = [12, 11, 13, 5, 6, 7]
heapsort(nums)
print(nums)
