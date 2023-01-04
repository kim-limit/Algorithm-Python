from collections import deque

n, k = map(int, input().split())

graph = []
virus = [[] for _ in range(k + 1)] # 바이러스 위치 지정

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n): # 처음 바이러스의 위치 저장
    for j in range(n):
        if graph[i][j] != 0:
            virus[graph[i][j]].append([i,j])

queue = deque()

for i in range(k + 1):
    if virus[i]: # 바이러스 우선순위대로 queue에 삽입
        for x, y in virus[i]:
            queue.append([x, y])


s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    lens = len(queue)
    for _ in range(lens):
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if graph[nx][ny] != 0:
                continue
            graph[nx][ny] = graph[x][y]
            queue.append([nx, ny])

for i in range(s): # 시간동안 bfs 돌림
    bfs()

print(graph[x-1][y-1])