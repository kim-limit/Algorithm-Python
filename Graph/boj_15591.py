from collections import deque
n, q = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y, c = map(int, input().split())
    graph[x].append((y, c)) # 노드 값 추가
    graph[y].append((x, c))

for _ in range(q):
    k, v = map(int, input().split())
    visited = [0] * (n + 1) # 방문 기록
    q = deque([(v, INF)])
    visited[v] = 1
    result = 0
    while q:
        v, cost = q.popleft()
        for next_v, next_cost in graph[v]: # 연결되 있는 노드중
            if visited[next_v] == 0 and min(cost, next_cost) >= k: # 더 작은 간선이 K 보다 크고 방문한적 없으면 go
                result += 1
                visited[next_v] = 1
                q.append([next_v, next_cost])
                
    print(result)