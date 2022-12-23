n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, dir = map(int, input().split())
# 0 북 1 동 2 남 3 서

d[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global dir
    dir -= 1
    if(dir == -1):
        dir = 3

count = 1
four_count = 0
while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 갈 수 있을때
    if(d[nx][ny] == 0 and arr[nx][ny] == 0):
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        four_count = 0
        continue
    # 갈 곳 없음
    else:
        four_count += 1
    # 4번 시도후
    if(four_count == 4):
        nx = x - dx[dir]
        ny = y - dy[dir]
        if(arr[nx][ny] == 0):
            x = nx
            y = ny
        else:
            break
        four_count = 0

print(count)