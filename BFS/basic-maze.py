from collections import deque
# 새로 가는 곳 마다 기존 값에서 +1 해주는 방식
# ex) 처음1 -> 다음가는곳 2 -> 3
n, m = map(int ,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append([0, 0])
    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            # 범위 벗어남
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            # 벽
            if graph[nx][ny] == 0:
                continue
            # 처음가는 곳만 갱신
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
    return graph[n - 1][m - 1]

print(bfs(0, 0))