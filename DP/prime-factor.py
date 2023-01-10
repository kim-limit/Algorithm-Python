n = int(input())

dp = [0] * n
dp[0] = 1

index2 = index3 = index5 = 0 # 각 배수들을 곱할 인덱스
next2, next3, next5 = 2, 3, 5 # 각 인덱스 마다의 배수 값

for i in range(1, n):
    # 배수값중 가장 작은 값 추가
    dp[i] = min(next2, next3, next5)
    # 중복도 있기 때문에 if로만
    if dp[i] == next2: 
        index2 += 1
        next2 = dp[index2] * 2
    if dp[i] == next3:
        index3 += 1
        next3 = dp[index3] * 3
    if dp[i] == next5:
        index5 += 1
        next5 = dp[index5] * 5

print(dp[n-1])