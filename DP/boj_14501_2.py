n = int(input())
t = []
p = []
dp  = [0] * (n + 1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1): # 거꾸로
    time = t[i] + i # 상담이 끝나는 일자
    if time <= n: # 상담을 할 수 있으면
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)