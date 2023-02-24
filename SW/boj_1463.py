n = int(input())

dp = [0] * (n + 4)

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    min_value = int(1e9)
    if i % 2 == 0: # 2로 나뉘어지는 경우
        min_value = min(dp[i // 2], min_value)
    if i % 3 == 0:
        min_value = min(dp[i // 3], min_value)
    dp[i] = min(min_value, dp[i - 1]) + 1

print(dp[n])