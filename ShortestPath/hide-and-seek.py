import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

## 그래프 생성 및 초기화
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [INF] * (n + 1)
# 최댓값 저장
max_value = -1e9
# 다익스트라
def dijkstra(start):
    global max_value
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
                if max_value < cost:
                    max_value = cost

dijkstra(1)

# 결과 출력
result = 0
count = 0
for i in range(n, 1, -1):
    print(i)
    if max_value == distance[i]:
        result = i
        count += 1

print(result, max_value, count)