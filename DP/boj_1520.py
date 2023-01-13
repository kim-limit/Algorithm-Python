from collections import deque

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir] 
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if array[nx][ny] < array[x][y]:
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dp = [[-1] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(dfs(0, 0))