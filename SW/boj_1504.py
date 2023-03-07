import heapq

def dijkstra(graph, distance, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = i[0] + dist
            if distance[i[1]] > cost:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [int(1e9)] * (n + 1)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

u, v = map(int, input().split())
distance_u = [int(1e9)] * (n + 1)
distance_v = [int(1e9)] * (n + 1)

dijkstra(graph, distance, 1) # start 1
dijkstra(graph, distance_u, u) # start u
dijkstra(graph, distance_v, v) # start v

case1 = distance[u] + distance_u[v] + distance_v[n] # 1 -> u -> v -> n
case2 = distance[v] + distance_v[u] + distance_u[n] # 1 -> v -> u -> n

result = min(case1, case2)
if result < int(1e9):
    print(result)
else:
    print(-1)