from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int ,input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

def bfs(v):
    queue = deque([v])
    while queue:
        start = queue.popleft()
        for next in graph[start]:
            # 처음 가는 곳이면 거리 초기화
            if distance[next] == -1:
                distance[next] = distance[start] + 1
                queue.append(next)

bfs(x)

# 결과 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        check = True
        print(i)

if not check:
    print(-1)