import heapq

INF = int(1e9)
    
t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(t):
    n = int(input())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]
    # 다익스트라
    q = []
    heapq.heappush(q, (graph[0][0], (0, 0)))
    distance[0][0] = graph[0][0]

    while q:
        dist, (x, y) = heapq.heappop(q)
        # 이미 했던건 건너뜀
        if distance[x][y] < dist:
            continue
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))

    print(distance[n-1][n-1])