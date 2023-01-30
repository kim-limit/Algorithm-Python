r, c, t = map(int, input().split())

graph = []
for i in range(r):
    graph.append(list(map(int, input().split())))

cleaner = []
# 공기청정기 위치 찾기
for i in range(r):
    if graph[i][0] == -1:
        cleaner.append(i)
        cleaner.append(i + 1)
        break

# 미세먼지 확산
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def spread():
    tmp_array = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if graph[x][y] != 0 and graph[x][y] != -1: # 미세먼지면
                tmp = 0
                spread_value = graph[x][y] // 5 # 확산되는 값
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if nx >= r or nx < 0 or ny >= c or ny < 0:
                        continue
                    if graph[nx][ny] == -1: # 공기청정기면 확산 x
                        continue
                    tmp_array[nx][ny] += spread_value
                    tmp += spread_value # 확산된 값 전체
                graph[x][y] -= tmp
    # 그래프 갱신
    for x in range(r):
        for y in range(c):
            graph[x][y] += tmp_array[x][y]

# 공기청정기 가동
def clean():
    start = cleaner[0] # 첫번째 공기 청정기
    prev = graph[start][1]
    graph[start][1] = 0

    for i in range(2, c - 1):
        graph[start][i], prev = prev, graph[start][i]
    for i in range(start, -1, -1):
        graph[i][c - 1] , prev = prev, graph[i][c - 1]
    for i in range(c - 2, 0, -1):
        graph[0][i], prev = prev, graph[0][i]
    for i in range(start):
        graph[i][0], prev = prev, graph[i][0]

    start = cleaner[1] # 두번째 공기청정기
    prev = graph[start][1]
    graph[start][1] = 0

    for i in range(2, c - 1):
        graph[start][i], prev = prev, graph[start][i]
    for i in range(start, r):
        graph[i][c - 1] , prev = prev, graph[i][c - 1]
    for i in range(c - 2, 0, -1):
        graph[r - 1][i], prev = prev, graph[r - 1][i]
    for i in range(r - 1, start, -1):
        graph[i][0], prev = prev, graph[i][0]

for i in range(t):
    spread()
    clean()

result = 0
for i in range(r):
    for j in range(c):
        if  graph[i][j] != -1:
            result += graph[i][j]
print(result)

