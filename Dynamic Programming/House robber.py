def houserobber(houses, currentindex):
    if currentindex >= len(houses):
        return 0
    else:
        stealfirsthouse = houses[currentindex] + houserobber(houses, currentindex + 2)
        skipfirsthouse = houserobber(houses, currentindex + 1)
        return max(stealfirsthouse, skipfirsthouse)
houses = [6,7,1,30,8,2,4]
print(houserobber(houses, 0))
