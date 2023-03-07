import heapq

def dijkstra(graph, distance, start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 지점
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 거리, 현재 노드
        if dist > distance[now]: # 이미 처리함
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split()) # 컴퓨터, 의존성 개수, 해킹 인덱스
    graph = [[] for _ in range(n + 1)]
    distance = [int(1e9)] * (n + 1)
    for i in range(d):
        a, b, s = map(int, input().split()) # b -> a, s: cost
        graph[b].append((s, a))

    dijkstra(graph, distance, c)
    count = 0
    time = 0
    for i in distance:
        if i != int(1e9):
            count += 1
            if time < i:
                time = i
    print(count, time)
