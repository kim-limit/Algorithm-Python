a = input()
b = input()

len_a = len(a)
len_b = len(b)
# 이차원 Dp 선언
dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
# 빈 문자열과 비교
for i in range(len_a + 1):
    dp[i][0] = i
for i in range(len_b + 1):
    dp[0][i] = i

for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        # 같은 알파벳이면 왼쪽 위 값으로 
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else: # 삭제, 교체, 삽입중 가장 작은수 + 1
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

print(dp[len_a][len_b])