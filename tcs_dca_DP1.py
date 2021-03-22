def minCoins(denoms,amount):
    coins=[float("inf") for i in range(amount+1)]
    coins[0]=0
    for denom in denoms:
        for amt in range(1,amount+1):
            if(denom<=amt):
                coins[amt]=min(coins[amt],coins[amt-denom]+1)
    return coins[amt] if coins[amt]!=float("inf") else -1
coins=[int(x) for x in input().split()]
amount=int(input())
print(minCoins(coins,amount))