import numpy as np
arr = np.array([10,20,30,40])
print(arr)
#insertion at front
arr1 = np.insert(arr, 0, 200)
print(arr1)

#insertion in the middle 
arr2=np.insert(arr, len(arr)//2, 400)
print(arr2)

#insertion at end
arr3 = np.insert(arr, len(arr), 500)
print(arr3)