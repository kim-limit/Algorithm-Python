import sys
def dfs(depth, index):
    global minValue
    # 반씩 나눠졌을 때
    if depth == n // 2:
        startSum = 0
        linkSum = 0

        for i in range(n - 1): # 더하기
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    startSum += array[i][j] + array[j][i]
                elif not visited[i] and not visited[j]:
                    linkSum += array[i][j] + array[j][i]
        minValue = min(minValue, abs(startSum - linkSum))
        return 
    # dfs
    for i in range(index, n):
        if visited[i]:
            continue
        visited[i] = True
        dfs(depth + 1, i + 1)
        visited[i] = False

input = sys.stdin.readline
n = int(input())

array = []
visited = [False] * n
for _ in range(n):
    array.append(list(map(int, input().split())))

minValue = int(1e9)
dfs(0, 0)
print(minValue)