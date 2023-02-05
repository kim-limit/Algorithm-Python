n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split()))) # 시간, 값

dp = [0] * (n + 1)

max_value = 0
for i in range(n - 1, -1, -1):
    if i + array[i][0] <= n: # 상담 가능
        dp[i] = max(dp[i + array[i][0]] + array[i][1], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
print(dp[0])