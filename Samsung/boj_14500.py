n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
max_value = int(-1e9)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# ㅗ 제외 확인
def dfs(x, y, depth, area):
    global max_value
    if depth == 3:
        max_value = max(max_value, area)
        return

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, depth + 1, area + array[nx][ny])
        visited[nx][ny] = False

# ㅗ 확인
def hdfs(x, y):
    global max_value
    # ㅗ ㅏ ㅜ ㅓ 확인
    for i in range(4):
        area = array[x][y]
        for j in range(3):
            nx = x + dx[(i + j) % 4]
            ny = y + dy[(i + j) % 4]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                break
            area += array[nx][ny]
        max_value = max(max_value, area)
        
        
            
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 0, array[i][j])
        visited[i][j] = False

        hdfs(i, j)

print(max_value)