def numberfactor(n, steps):
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):
        for step in steps:
            if i - step >= 0:
                dp[i] += dp[i - step]
    return dp[n]
print(numberfactor(4, [1, 3, 4]))   
print(numberfactor(5, [1, 3, 4]))   
print(numberfactor(6, [1, 3, 4]))   