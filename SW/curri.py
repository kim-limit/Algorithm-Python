from collections import deque
import copy

def topology():
    q = deque([])
    result = copy.deepcopy(time)
    for i in range(1, n):
        if indegree[i] == 0: 
            q.append(i)

    while q: # 위상정렬
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1 # 2, 3
            if indegree[i] == 0:
                q.append(i)
        
    for i in range(1, n + 1):
        print(result[i])


n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    for j in arr[1:-1]: # 진입 노드 설정
        graph[j].append(i)
        indegree[i] += 1

topology()