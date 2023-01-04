from collections import deque

n, m = map(int, input().split())
area = 0
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

temp = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b): # 바이러스 퍼트릴떄 bfs
    queue = deque([[a, b]])
    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if temp[nx][ny] != 0:
                continue
            temp[nx][ny] = 2
            queue.append([nx, ny])

def dfs(count):
    global area

    if count == 3: # 울타리 3개지으면 
        # 새 배열에 현재 그래프 상태 할당
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 바이러스 위치마다 bfs 돌림
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    bfs(i, j)
        # 결과 출력
        result = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    result += 1

        area = max(area, result)
        # dfs 끝내줘야 하니까 return
        return 
    # i부터 j까지 다 돌면서 울타리 3개 지음
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                # 3개지으면 return 받아서 재귀 끝 -> 0으로 초기화 해야함
                graph[i][j] = 0
                count -= 1


dfs(0)

print(area)