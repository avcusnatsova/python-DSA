class item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight
def knapsackmethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse = True)
    usedcapacity = 0
    totalvalue = 0

    for i in items:
        if usedcapacity + i.weight <= capacity:
            usedcapacity += i.weight
            totalvalue += i.value
        else:
            unusedweight = capacity - usedcapacity
            value = i.ratio * unusedweight
            usedcapacity += unusedweight
            totalvalue += value
        if usedcapacity == capacity:
            break
    print("total value obtained: " +str(totalvalue))
item1 = item(20,100)
item2 = item(30,120)
item3 = item(10,60)
clist = [item1, item2, item3]

knapsackmethod(clist, 50)

