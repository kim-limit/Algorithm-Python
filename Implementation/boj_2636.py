from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
area = []

def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if visited[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0: # 공기일때
                visited[nx][ny] = 1
                q.append([nx, ny])
            else:
                graph[nx][ny] = 0 # 녹이기
                visited[nx][ny] = 1
                cnt += 1
    area.append(cnt)
    return cnt

time = 0
while True:
    time +=1
    visited = [[0] * m for _ in range(n)]
    cnt = bfs() 
    if cnt == 0:
        break

print(time-1)
print(area[-2])
