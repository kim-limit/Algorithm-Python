n = int(input())

dp = [[3, 2]]

if n % 2 == 0:    
    for i in range(1, n):
        correct = dp[i - 1][0] * 3 + dp[i - 1][1]
        fail = dp[i - 1][0] * 2 + dp[i - 1][1]
        dp.append([correct, fail])
    print(dp[n // 2 - 1][0])
else:
    print(0)
