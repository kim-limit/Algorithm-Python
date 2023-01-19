n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 최대
def get_max(array):
    dp = [array[0][0], array[0][1], array[0][2]] # 첫번째 줄로 초기화
    for i in range(1, n):
        a = max(dp[0], dp[1]) + array[i][0] # 첫번째
        b = max(dp[0], dp[1], dp[2]) + array[i][1] # 두번쨰
        c = max(dp[1], dp[2]) + array[i][2] # 세번째
        # 미리 할당하면 값바뀜 -> 나중에 초기화
        dp[0] = a
        dp[1] = b
        dp[2] = c

    return(max(dp))

# 최소 (최대 반대로 하면 됨)
def get_min(array):
    dp = [array[0][0], array[0][1], array[0][2]]
    for i in range(1, n):
        a = min(dp[0], dp[1]) + array[i][0]
        b = min(dp[0], dp[1], dp[2]) + array[i][1]
        c = min(dp[1], dp[2]) + array[i][2]
        dp[0] = a
        dp[1] = b
        dp[2] = c

    return(min(dp))

print(get_max(array), end = " ")
print(get_min(array), end = " ")