n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위 벗어남
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    if graph[x][y] == 0:
        # 1이면 못감 -> 방문도 1로 설정해 주면됨
        graph[x][y] = 1
        dfs(x + 1, y)
        dfs(x - -1 ,y)
        dfs(x, y + 1)
        dfs(x, y + 1)
        return True
    return False
    

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1