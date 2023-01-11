n = int(input())
# n이 1, 2인경우 런타임 날 수 있으니 301개 만들고 값 변경
stair = [0] * 301
for i in range(1, n + 1): 
    stair[i] = int(input())

dp = [0] * 301
dp[1] = stair[1] # 첫번 째 칸 올라가는 경우
dp[2] = stair[1] + stair[2] # 두번째 칸 올라가는 경우
dp[3] = max(stair[1], stair[2]) + stair[3] # 세번째 칸 올라가는 경우

for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stair[i - 1], dp[i - 2]) + stair[i]

print(dp[n])