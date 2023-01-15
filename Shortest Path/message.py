import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
# 도시 개수, 통로 개수, 시작점
n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)] # 간선 정보
distance = [INF] * (n + 1) # 거리 정보

for _ in range(m):
    # 시작, 도착, 거리
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstr(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 방문 했던곳은 넘어감
            continue
        for i in graph[now]: # i[0] 도착, i[1] 거리
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
dijkstr(c)

# 결과 출력
count = 0
max = -1
for i in range(1, n + 1):
    if distance[i] > 0:
        count += 1
    if distance[i] > max:
        max = distance[i]

print(count, end = ' ')
print(max)
