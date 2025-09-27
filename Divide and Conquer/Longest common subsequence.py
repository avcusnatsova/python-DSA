def findlcs(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + findlcs(s1, s2, index1+1, index2+1)
    else:
        op1 = findlcs(s1, s2, index1, index2+1)
        op2 = findlcs(s1, s2, index1+1, index2)
        return max(op1, op2)
print(findlcs("elephant" , "eretpat", 0,0))