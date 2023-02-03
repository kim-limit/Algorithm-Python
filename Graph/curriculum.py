from collections import deque
import copy
n = int(input())

graph = [[] for _ in range(n + 1)] # 연결되 있는 애들 저장
indegree = [0] * (n + 1) # 진입차수
time = [0] * (n + 1) # 강의 시간

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1 # 선수 강의가 있으면 진입차수 +
        graph[j].append(i) # 선수강의에 현재 강의 추가

result = copy.deepcopy(time)
q = deque()
for i in range(1, n + 1): # 진입차수 0인거 추가
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        result[i] = max(result[i], result[now] + time[i]) # 선수 강의 시간 초기화
        indegree[i] -= 1 # 진입 차수 줄임
        if indegree[i] == 0: # 새로 0된애들 추가
            q.append(i) 

for i in range(1, n + 1):
    print(result[i])