shape = [[0, -1, 1, 0], [-1, 0, 0, -1], [-1, 0, 0, 1], [0, 1, 1, 0]]

def dfs(x, y, result):
    global max_value
    if y == m:
        x += 1
        y = 0
    if x == n:
        max_value = max(max_value, result)
        return
    if not visited[x][y]:
        for dir in range(4):
            a, b, c, d = shape[dir]
            nx1 = x + a
            ny1 = y + b
            nx2 = x + c
            ny2 = y + d
            if 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < m and 0 <= ny2 < m: # 범위
                if not visited[nx1][ny1] and not visited[nx2][ny2]: # 방문 x
                    visited[nx1][ny1] = visited[nx2][ny2] = visited[x][y] = True
                    dfs(x, y + 1, result + graph[nx1][ny1] + graph[x][y] * 2 + graph[nx2][ny2])
                    visited[nx1][ny1] = visited[nx2][ny2] = visited[x][y] = False

    dfs(x, y + 1, result) # 끝까지 못갔어도 한칸은 내려가야하니까

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

max_value = -1
dfs(0, 0, 0)

print(max_value)