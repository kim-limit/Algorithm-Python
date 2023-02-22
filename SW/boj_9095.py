t = int(input())

dp = [0] * 11 # dp 배열 초기화
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1] 

for _ in range(t):
    n = int(input())
    print(dp[n - 1])