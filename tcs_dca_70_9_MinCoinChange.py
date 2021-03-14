def minNoOfCoins(amount,denoms):
    coins=[float("inf") for i in range(amount+1)]
    coins[0]=0
    for denom in denoms:
        for amt in range(denom,amount+1):
            coins[amt]=min(coins[amt],coins[amt-denom]+1)
        print(coins)
    return coins[amount] if coins[amount]!=float("inf") else 0
amount=int(input())
denoms=[int(x) for x in input().split()]
print(minNoOfCoins(amount,denoms))