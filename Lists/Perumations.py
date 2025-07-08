#when two list contains the same elements but in different order

def permutations(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 ==  list2:
        return True
    else:
        return False
l1 = [1,2,3]
l2 = [1,3,2]
print(permutations(l1, l2))