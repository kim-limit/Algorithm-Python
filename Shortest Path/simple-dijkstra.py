import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)] # 그래프
visited = [False] * (n + 1) # 방문 기록
distance = [INF] * (n + 1) # 거리

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 현재 거리 배열중에 가장 작은거 고르기 (이미 방문한거 빼고)
def get_smallest_node(): 
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작점과 시작점에서 갈 수 있는곳 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        # 만약 더 작으면 갱신
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])