r, c, k = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * c for _ in range(r)]

result = 0
def dfs(x, y, count):
    global  visited, result
    if x == 0 and y == c - 1:
        if count == k:
            result += 1
            
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx >= r or nx < 0 or ny >= c or ny < 0:
            continue
        if visited[nx][ny] == 0 and graph[nx][ny] != 'T':
            visited[nx][ny] = 1
            dfs(nx, ny, count + 1)
            visited[nx][ny] = 0

visited[r-1][0] = 1
dfs(r - 1, 0, 1)

print(result)