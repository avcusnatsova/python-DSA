def numberofpaths(twodarray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twodarray[0][0] == cost:
            return 1
        else:
            return 0
    elif row == 0:
        return numberofpaths(twodarray, 0, col-1, cost - twodarray[row][col])
    elif col == 0:
        return numberofpaths(twodarray, row-1, 0, cost - twodarray[row][col])
    else:
        op1 = numberofpaths(twodarray, row-1, col, cost - twodarray[row][col])
        op2 = numberofpaths(twodarray, row, col-1, cost - twodarray[row][col])
        return op1 + op2


twodlist = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 1, 2],
    [7, 1, 6, 3]
]

result = numberofpaths(twodlist, 3, 3, 25)
print("Number of paths:", result)
