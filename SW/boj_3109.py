dx = [-1, 0, 1] # 오른쪽 위로 먼저가야 최적
def dfs(x, y):
    if y == c - 1:
        return True
    for dir in range(3):
        nx = x + dx[dir]
        ny = y + 1
        if nx >= r or nx < 0 or ny >= c or ny < 0:
            continue
        if visited[nx][ny] == 0 and arr[nx][ny] != 'x':
            visited[nx][ny] = 1 # 방문 하고 안지움 -> 그길로 이미 갔는데 못간거면 어차피 못가는 길임
            if dfs(nx, ny): # [-1, 0, 1 ] 중에 갈 수 있는 길이 있으면 그길만 가고 끝냄
                return True
    return False

r, c = map(int, input().split())

arr = []
for _ in range(r):
    arr.append(list(input()))

visited = [[0] * c for _ in range(r)]
result = 0

for i in range(r):
    if dfs(i, 0):
        result += 1
print(result)