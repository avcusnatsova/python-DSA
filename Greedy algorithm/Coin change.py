def coinchange(totalnumber, coins):
    n = totalnumber
    coins.sort()
    index = len(coins) - 1
    while True:
        coinvalue = coins[index]
        if n >= coinvalue:
            print(coinvalue)
            n = n - coinvalue
        if n < coinvalue:
            index -= 1
        if n == 0:
            break
coins = [1, 2, 5, 20, 50, 100]
total = 201

coinchange(total, coins)
