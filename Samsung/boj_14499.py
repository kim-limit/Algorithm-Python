n, m, x, y, k= map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

moves = list(map(int, input().split()))

# 주사위
dice = [[0, 0, 0, 0], [0, 0, 0, 0]]

# 동1 서2 북3 남4
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in moves:
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]

    if nx >= n or nx < 0 or ny >= m or ny < 0:
        continue
    # 움직임
    if i == 1: # 동
        temp = dice[0].pop(-1)
        dice[0].insert(0, temp)
        dice[1][0] = dice[0][0]
        dice[1][2] = dice[0][2]
    elif i == 2: # 서
        temp = dice[0].pop(0)
        dice[0].append(temp)
        dice[1][0] = dice[0][0]
        dice[1][2] = dice[0][2]
    elif i == 3: # 남
        temp = dice[1].pop(-1)
        dice[1].insert(0, temp)
        dice[0][0] = dice[1][0]
        dice[0][2] = dice[1][2]
    else: # 북
        temp = dice[1].pop(0)
        dice[1].append(temp)
        dice[0][0] = dice[1][0]
        dice[0][2] = dice[1][2]

    # 바닥 복사
    if array[nx][ny] == 0:
        array[nx][ny] = dice[0][2]
    else:
        dice[0][2] = array[nx][ny]
        dice[1][2] = array[nx][ny]
        array[nx][ny] = 0

    x = nx
    y = ny
    # 위 출력
    print(dice[0][0])