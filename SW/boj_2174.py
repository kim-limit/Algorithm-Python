a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[0] * b for _ in range(a)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

robot = []
for i in range(n):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    graph[x - 1][y - 1] = i + 1 # 로봇 위치
    dir = 0
    if c == 'W':
        dir = 0
    elif c == 'N':
        dir = 1
    elif c == 'E':
        dir = 2
    else:
        dir = 3
    robot.append([x - 1, y - 1, dir])

moves = []
for _ in range(m):
    moves.append(list(input().split()))

def check(moves, robot):
    for index, t, n in moves: # 로봇, 명령, 횟수
        index = int(index)
        n = int(n)
        x, y, dir = robot[index - 1]
        for i in range(n):
            if t == 'L':
                dir = (dir + 3) % 4
            elif t == 'R':
                dir = (dir + 1) % 4
            else : # 이동
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx >= a or nx < 0 or ny >= b or ny < 0: # 벽
                    print('Robot {} crashes into the wall'.format(index))
                    return False
                if graph[nx][ny] != 0:
                    print('Robot {} crashes into robot {}'.format(index, graph[nx][ny]))
                    return False
                graph[x][y] = 0
                graph[nx][ny] = index
                x = nx
                y = ny
        robot[index - 1][0] = x
        robot[index - 1][1] = y
        robot[index - 1][2] = dir
    return True

if check(moves, robot):
    print('OK')