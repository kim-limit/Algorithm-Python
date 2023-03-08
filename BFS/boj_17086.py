from collections import deque

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, -1, 0, 1, -1, 0, 1, -1 ]
def bfs():
    while q:
        x, y = q.popleft()
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

n, m = map(int, input().split())

graph = []
q = deque([])
visited = [[0] * m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 1 # 상어 위치는 1        

bfs()
max_value = -1
for i in range(n):
    max_value = max(max(visited[i]), max_value)

print(max_value - 1)