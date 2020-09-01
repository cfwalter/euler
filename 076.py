target = 100
coins = list(range(1, 100))
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print(ways[-1])
