from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(graph, visited, n):
    q = deque([[0, 0]])
    visited[0][0] = graph[0][0]

    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if visited[nx][ny] > visited[x][y] + graph[nx][ny]:
                visited[nx][ny] = visited[x][y] + graph[nx][ny]
                q.append([nx, ny])
    return visited

index = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[int(1e9)] * n for _ in range(n)]
    bfs(graph, visited, n)
    print('Problem {}: {}'.format(index, visited[n-1][n-1]))
    index += 1
