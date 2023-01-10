from bisect import bisect_left

n = int(input())

array = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[j] + 1, dp[i])

max_value = max(dp)
max_index = dp.index(max_value)

result = []
for value in range(max_value, 0, -1):
    while dp[max_index] != value:
        max_index -= 1
    result.append(array[max_index])
    max_index -= 1

result.reverse()
print(max_value)        
print(*result)
