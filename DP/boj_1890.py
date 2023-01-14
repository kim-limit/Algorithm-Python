def dfs(x, y):
    if x == n - 1 and y == n -1: # 마지막 방문시
        return 1
    if dp[x][y] == -1: # 처음 간 곳만
        dp[x][y] = 0 # 방문 체크
        for dir in range(2):
            nx = x + array[x][y] * dx[dir]
            ny = y + array[x][y] * dy[dir]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dp = [ [-1] * n for _ in range(n) ]
dx = [1, 0]
dy = [0, 1]

print(dfs(0, 0))
