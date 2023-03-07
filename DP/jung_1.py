n = int(input())

dp = [0] * (n + 1)
dp[0] = 1
arr = list(map(int, input().split()))
index = max(arr) # 최대 인덱스
for i in arr:
    dp[i] += 1

if dp[2] != 0:
    dp[2] += dp[0]

case = list(set(arr))
for i in range(3, n):
    if i in case:
        dp[i] += max(dp[i - 2], dp[i - 3])
    
print(max(dp))