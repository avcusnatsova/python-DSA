dict3 = dict(one = 1, two = 2, three = 3)
print(dict3)

def linearsearch(dict, value):
    for key in dict:
        if dict[key] == value:
            return key,value

    return 'value not found'
print (linearsearch(dict3, 2))        
