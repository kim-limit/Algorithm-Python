n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 플로이드 워셜
for a in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][a] + graph[a][j])

# dfs
min_value = int(1e9)

visited = [0] * n
def dfs(depth, time, x):
    global min_value, visited

    if depth == n - 1:
        min_value = min(min_value, time)
        return
    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(depth + 1, time + graph[x][i], i)
        visited[i] = 0

visited[k] = 1
dfs(0, 0, k)
print(min_value)