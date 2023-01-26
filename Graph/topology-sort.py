from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1) # 진입차수
graph = [[] for i in range(v + 1)] # 간선 정보 ex) 노드 1 -> 2, 3연결

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 간선 정보
    indegree[b] += 1 # 진입 차수 + 1

def topology_sort():
    result = [] 
    q = deque()

    for i in range(1, v + 1): # 처음에 진입차수 0인거 큐에 넣음
        if indegree[i] == 0:
            q.append(i)
    
    while q: # 큐가 빌때까지
        now = q.popleft()
        result.append(now) # 결과에 넣음
        for i in graph[now]: # 현재 노드에서 연결된 간선 제거
            indegree[i] -= 1 # 진입차수 1개 줄임
            if indegree[i] == 0: # 새롭게 진입차수 0 된애 큐에 넣어줌
                q.append(i)
    
    for i in result:
        print(i, end = " ")

topology_sort()