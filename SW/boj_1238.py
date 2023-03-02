import heapq

def dijkstra(start):
    distance = [int(1e9)] * (n + 1)
    q = []
    heapq.heappush(q, (0, start)) # 시작점 추가
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 확인할 노드의 간선 크기
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = i[0] + dist # 현재 노드의 크기와 간선 크기
            if cost < distance[i[1]]: 
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    
    return distance


n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))

result = dijkstra(x) # x에서 갈 수 있는 최단 경로
for i in range(1, n + 1):
    if i != x: # 모든 노드에서 x로 가는 최단 경로
        tmp = dijkstra(i)
        result[i] += tmp[x]

print(max(result[1:]))