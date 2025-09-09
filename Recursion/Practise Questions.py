#sum of digits
def sumofdigits(n):
    assert n>= 0 and int(n) == n, 'The number has to be a positive number'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofdigits(int(n/10))
print(sumofdigits(1111111))

#power

def power(base,exp):
    if exp ==0:
        return 1
    if exp == 1:
        return (base)
    if exp != 1:
        return (base*power(base, exp -1))
    
print(power(4,2))

#gcd

def gcd(a,b):
    assert int(a) == a and int(b) == b, 'the numbers must be integer only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
print(gcd(12, 6))

#decimal to binary
def decimaltobinary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimaltobinary(int(n/2))
    
print(decimaltobinary(1))