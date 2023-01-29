n = int(input())

graph = [[0] * 101 for _ in range(101)]

# 0, 1, 2, 3
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):
    y, x, d, g = map(int, input().split())
    # 커브 리스트
    curve = [d] # 0 세대
    for j in range(g):
        # 1, 2, 4, 8
        lens = len(curve)
        for k in range(lens): # 대칭으로 한바퀴
            curve.append((curve[lens - 1 - k] + 1) % 4)
    graph[x][y] = 1
    for dir in curve:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx > 100 or nx < 0 or ny > 100 or ny < 0:
            continue
        graph[nx][ny] = 1
        x = nx
        y = ny

answer = 0
for i in range(100):
    for j in range(100):
        # 네모 모양이면 정답 + 1
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)