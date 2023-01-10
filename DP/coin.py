n, m = map(int, input().split())
d = [10001] * 10001

coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

d[0] = 0
for coin in coins:
    for i in range(coin, m + 1):
        if d[i - coin] != 10001:
            d[i] = min(d[i], d[i - coin] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])