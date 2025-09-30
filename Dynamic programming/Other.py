# House Robber - iterative DP (O(n) time, O(1) space)
def house_robber(nums):
    """
    Given a list nums of non-negative integers (amounts in houses),
    returns the maximum amount that can be robbed without robbing two adjacent houses.
    """
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]

    prev2 = 0        # dp[i-2]
    prev1 = nums[0]  # dp[0]
    for i in range(1, n):
        cur = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, cur
    return prev1

# Example
print(house_robber([2,7,9,3,1]))  # -> 12 (rob 2 + 9 + 1)
# Edit Distance - Top-down (memoized recursion)
def edit_distance_td(s1, s2):
    from functools import lru_cache

    @lru_cache(None)
    def dp(i, j):
        # minimum ops to convert s1[i:] -> s2[j:]
        if i == len(s1):   # need insert remaining s2 chars
            return len(s2) - j
        if j == len(s2):   # need delete remaining s1 chars
            return len(s1) - i
        if s1[i] == s2[j]:
            return dp(i+1, j+1)
        # options: insert (insert s2[j] before s1[i]), delete (delete s1[i]), replace
        insert = 1 + dp(i, j+1)
        delete = 1 + dp(i+1, j)
        replace = 1 + dp(i+1, j+1)
        return min(insert, delete, replace)

    return dp(0, 0)


# Edit Distance - Bottom-up tabulation
def edit_distance_bu(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    # base cases
    for i in range(n-1, -1, -1):
        dp[i][m] = n - i  # delete remaining chars in s1
    for j in range(m-1, -1, -1):
        dp[n][j] = m - j  # insert remaining chars from s2

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1 + min(dp[i][j+1],   # insert
                                   dp[i+1][j],   # delete
                                   dp[i+1][j+1]) # replace
    return dp[0][0]


# Example usage
a = "intention"
b = "execution"
print("TD:", edit_distance_td(a, b))  # -> 5
print("BU:", edit_distance_bu(a, b))  # -> 5
# 0/1 Knapsack - Top-down with memoization
def knapsack_td(values, weights, capacity):
    from functools import lru_cache
    n = len(values)
    @lru_cache(None)
    def dp(i, cap):
        # maximum profit using items[i:] with remaining capacity cap
        if i == n or cap == 0:
            return 0
        if weights[i] > cap:
            return dp(i+1, cap)
        # choose max of taking or skipping
        take = values[i] + dp(i+1, cap - weights[i])
        skip = dp(i+1, cap)
        return max(take, skip)
    return dp(0, capacity)


# 0/1 Knapsack - Bottom-up tabulation
def knapsack_bu(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n+1)]
    # dp[i][c] = max profit using items[i:] with capacity c
    # Build from bottom: i from n-1 down to 0
    for i in range(n-1, -1, -1):
        for c in range(capacity + 1):
            if weights[i] > c:
                dp[i][c] = dp[i+1][c]
            else:
                dp[i][c] = max(dp[i+1][c], values[i] + dp[i+1][c-weights[i]])
    return dp[0][capacity]


# Space-optimized bottom-up (1D)
def knapsack_bu_1d(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)
    # iterate items
    for i in range(n):
        # iterate capacity backwards to avoid reuse
        for c in range(capacity, weights[i]-1, -1):
            dp[c] = max(dp[c], values[i] + dp[c - weights[i]])
    return dp[capacity]


# Example
vals = [60, 100, 120]
wts = [10, 20, 30]
cap = 50
print("TD:", knapsack_td(vals, wts, cap))       # -> 220
print("BU:", knapsack_bu(vals, wts, cap))       # -> 220
print("BU 1D:", knapsack_bu_1d(vals, wts, cap)) # -> 220
