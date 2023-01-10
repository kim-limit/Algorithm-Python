from bisect import bisect_left

n = int(input())

array = list(map(int, input().split()))

dp = [array[0]]

for i in range(1, n):
    if array[i] > dp[-1]:
        dp.append(array[i])
    else:
        index = bisect_left(dp, array[i]) # 현재 값보다 큰 수 찾음
        dp[index] = array[i]

print(len(dp))