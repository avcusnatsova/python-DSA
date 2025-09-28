#top down
def numberfactor(n, memo={}):
    if n == 0 or n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    if n in memo:
        return memo[n]
    
    sub1 = numberfactor(n-1, memo)
    sub2 = numberfactor(n-3, memo)
    sub3 = numberfactor(n-4, memo)

    memo[n] = sub1 + sub2 + sub3
    return memo[n]
print(numberfactor(4))
print(numberfactor(5))

#bottom up
def numfactor(n):
    dp = [0] * (n+1)

    dp[0] = dp[1] = dp[2] = 1
    dp[3] = 2

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3] +dp[i-4]
    return dp[n]
print(numfactor(6))