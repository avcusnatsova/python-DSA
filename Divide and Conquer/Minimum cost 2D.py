def findmincost(twodarray, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return twodarray[0][0]
    else:
        op1 = findmincost(twodarray, row-1, col)
        op2 = findmincost(twodarray, row, col-1)

        return twodarray[row][col] + min(op1, op2)
twodlist = [[4,7,8,6,4],
           [6,7,3,9,2],
           [3,8,1,2,4],
           [7,1,7,3,7],
           [2,9,8,9,3]
           ]

print(findmincost(twodlist, 4,4))