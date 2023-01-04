from collections import deque
n, l, r = map(int , input().split())

graph = []

visited = [[0] * n for _ in range(n)]

for i in range(n):
    graph.append(list(map(int ,input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque([[i, j]])  
    visited[i][j] = 1
    visited_index = [] # 연합 나라 위치
    country = 0 # 연합 나라의 합
    size = 0  # 연합 나라의 수
    while queue:
        x, y = queue.popleft()
         # 큐에 있었으면 연합이었다는 뜻
        visited_index.append([x, y]) 
        country += graph[x][y]
        size += 1  # 크기와 갯수 index 추가
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if visited[nx][ny] == 1:
                continue
            if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                queue.append([nx,ny])
                visited[nx][ny] = 1
    return country, size, visited_index

count = 0 # 인구 이동 발생하는 횟수
while True:
    break_point = False
    visited = [[0] * n for _ in range(n)] # 방문 체크 한바퀴마다 초기화
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0: # 방문 안한곳은 bfs 돌림
                country, size, visited_index = bfs(i, j) # 인접 나라 크기, 나라수, 나라 index 받아옴
                if size > 1: # 만약 인구이동이 일어나면 break point -> true
                    break_point = True
                for x, y in visited_index: # 연합인구로 변경
                    graph[x][y] = int(country / size)
    if not break_point:
        break
    count += 1

print(count)