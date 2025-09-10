# -------------------------
# Power Function
# -------------------------
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


# -------------------------
# Factorial Function
# -------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# -------------------------
# Product of Array
# -------------------------
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])


# -------------------------
# Recursive Range
# -------------------------
def recursiveRange(n):
    if n == 0:
        return 0
    return n + recursiveRange(n - 1)


# -------------------------
# Fibonacci
# -------------------------
def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


# -------------------------
# Reverse String
# -------------------------
def reverse(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse(s[:-1])


# -------------------------
# Palindrome Check
# -------------------------
def isPalindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])


# -------------------------
# Some Recursive
# -------------------------
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if cb(arr[0]):
        return True
    return someRecursive(arr[1:], cb)


# -------------------------
# Flatten Array
# -------------------------
def flatten(arr):
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# -------------------------
# Capitalize First Letter
# -------------------------
def capitalizeFirst(arr):
    if len(arr) == 0:
        return []
    first = arr[0][0].upper() + arr[0][1:] if arr[0] else ""
    return [first] + capitalizeFirst(arr[1:])


# -------------------------
# Nested Even Sum
# -------------------------
def nestedEvenSum(obj):
    total = 0
    for key, value in obj.items():
        if type(value) == int and value % 2 == 0:
            total += value
        elif isinstance(value, dict):
            total += nestedEvenSum(value)
    return total


# -------------------------
# Capitalize Words
# -------------------------
def capitalizeWords(arr):
    if len(arr) == 0:
        return []
    first = arr[0].upper() if arr[0] else ""
    return [first] + capitalizeWords(arr[1:])


# -------------------------
# Stringify Numbers
# -------------------------
def stringifyNumbers(obj):
    new_obj = {}
    for key, value in obj.items():
        if type(value) == int:
            new_obj[key] = str(value)
        elif isinstance(value, dict):
            new_obj[key] = stringifyNumbers(value)
        else:
            new_obj[key] = value
    return new_obj


# -------------------------
# Collect Strings
# -------------------------
def collectStrings(obj):
    strings = []
    for key, value in obj.items():
        if isinstance(value, str):
            strings.append(value)
        elif isinstance(value, dict):
            strings.extend(collectStrings(value))
    return strings
