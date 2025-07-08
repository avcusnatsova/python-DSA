dict1 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "5" : "five"
}

d2 = {0: "zero", 1: "one"}

#print(dict1)
#print('four' in dict1)
#print('six' not in dict1)
#print(len(dict1))

# all()

#true
#print(all(dict1))

#false -- zero
#print(all(d2))

#false -- none
d3 = {"": "empty", "name": "Alice"}
#print(all(d3))

#true -- empty
d4 = {}
#print(all(d4))

#any()
'''print(any(dict1))
print(any(d2))
print(any(d3))
print(any(d4))'''

print(sorted(dict1))