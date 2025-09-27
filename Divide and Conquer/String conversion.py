def findminoperation(s1, s2, i, j):
    if i == len(s1):   #insert
        return len(s2) - j
    if j == len(s2):   #delete
        return len(s1)- i
    if s1[i] == s2[j]:
        return findminoperation(s1, s2, i+1, j+1)
    
    else:
        deleteop = 1 + findminoperation(s1, s2, i+1, j)
        insertop = 1 + findminoperation(s1, s2, i, j+1)
        replaceop = 1 + findminoperation(s1, s2, i+1, j+1)
        return min(deleteop, insertop, replaceop)
print(findminoperation("table", "tbrltt", 0, 0))
