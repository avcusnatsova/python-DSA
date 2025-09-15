def mod(number, cellnumber):
    return number % cellnumber
print(mod(400, 24))

def modASCII(string, cellnumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellnumber
print(modASCII("CUSNAT", 24))