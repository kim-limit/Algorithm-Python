from collections import deque

def topology():
    result = []
    q = deque([])
    for i in range(1, n + 1): # 진입 차수 0인거
        if indegree[i] == 0:
            q.append(i)

    while q: # 큐 빌때까지
        now = q.popleft()
        result.append(now) # 결과에 추가

        for i in graph[now]: # 현재 노드에서 갈 수 있는 곳
            indegree[i] -= 1 # 진입차수 하나 내림 
            if indegree[i] == 0: # 진입차수 0되면
                q.append(i) # 큐에 다시 추가

    return result

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = topology()
print(*result)