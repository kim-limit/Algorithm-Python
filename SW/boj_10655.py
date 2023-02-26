n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

total = 0
for i in range(1, n): # 전체 길이
    total += abs(arr[i][0] - arr[i - 1][0]) + abs(arr[i][1] - arr[i - 1][1])

max_value = -1
for i in range(1, n - 2): # 건너뛰었을때 안건너뛴 거랑 차이가 가장 큰값 구함
    skip = abs(arr[i + 1][0] - arr[i - 1][0]) + abs(arr[i + 1][1] - arr[i - 1][1]) # 건너뛸때
    nonSkip = abs(arr[i][0] - arr[i - 1][0]) + abs(arr[i][1] - arr[i - 1][1]) + abs(arr[i][0] - arr[i + 1][0]) + abs(arr[i][1] - arr[i + 1][1]) # 안건너뜀
    max_value = max(nonSkip - skip, max_value)

print(total - max_value)
