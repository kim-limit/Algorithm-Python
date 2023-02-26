v = int(input())

visited = [-1] * (v + 1)
def dfs(start, d):
    for next, c in graph[start]: # 모든 간선 확인
        if visited[next] == -1: # 안간 곳
            visited[next] = c + d # 지금까지 간선 값
            dfs(next, c + d) 

graph = [[] for _ in range(v + 1)]
for _ in range(v): # 간선 정보 입력
    w = list(map(int, input().split()))
    for i in range(1, len(w) - 2, 2):
        graph[w[0]].append([w[i], w[i + 1]])

visited[1] = 0
dfs(1, 0) # 1에서 제일 먼 곳 찾기

start = visited.index(max(visited)) # 제일 먼곳
visited = [-1] * (v + 1)
visited[start] = 0
dfs(start, 0)
print(max(visited))