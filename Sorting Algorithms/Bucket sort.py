import math

def bucketsort(nums):
    n = len(nums)
    if n == 0:
        return nums
    
    minval,maxval= min(nums), max(nums)

    if minval == maxval:
        return nums[:]
    bucketcount = max(1, round(math.sqrt(n))) #math.sqrt --> square root of elements, then take the round of, from 1 because ensures atleast one bucket exist
    buckets = [[] for _ in range(bucketcount)]

    for num in nums:
        idx = int((num - minval) / (maxval - minval) * (bucketcount - 1)) #formula is to map smallest num to first and largest to last bucket
        #* (bucket_count - 1) --> 
        #bucket_count = 4 → indices should be [0,1,2,3] 
        #num = 23 → int(0.5238) = 0 → goes to bucket 0
        buckets[idx].append(num)

    result = []
    for b in buckets:
        result.extend(sorted(b))
    return result
if __name__ == "__main__":
    numbers = [42, 32, 23, 52, 25, 47, 51, 19, 75, 12]
    print("Original list:", numbers)

    sorted_numbers = bucketsort(numbers)
    print("Sorted list:  ", sorted_numbers)