def turn_dir(dir, c): # 회전시키는 함수
    if c == 'L':
        return (dir + 3) % 4 
    else: 
        return (dir + 1) % 4

def print_map(map): # 맵 확인용
    for i in range(len(map)):
        print(map[i])

def solution():

    n = int(input())
    maps = [[0] * (n + 1) for _ in range(n + 1)] # n + 1크기의 배열 생성

    k = int(input())
    # 사과 2
    # 뱀위치 1
    for _ in range(k):  # 맵에 사과 위치 2로 지정
        x, y = map(int ,input().split())
        maps[x][y] = 2

    l = int(input())
    turn = [] # (시간, 회전) 리스트
    for _ in range(l):
        x, c = input().split()
        turn.append([int(x), c])

    x, y = 1, 1  # 뱀의 첫위치
    maps[x][y] = 1

    dx =[0, 1, 0, -1]  #상하좌우 방향
    dy =[1, 0, -1, 0]

    dir = 0 # 처음은 오른쪽
    time = 0 # 시간
    turn_index = 0 # 회전

    snake_index = [[x,y]] # 뱀의 위치 저장
    while True:
        x += dx[dir]  # 1칸이동
        y += dy[dir]
        if x <= n and y <= n and x >=1 and y >= 1 and maps[x][y] != 1: # 벽이나 몸에 안부딫힌 경우
            if maps[x][y] != 2: # 사과없음
                px, py = snake_index.pop(0)  # 꼬리 한칸이동
                maps[px][py] = 0
            maps[x][y] = 1
            snake_index.append([x,y]) # 어차피 머리는 움직이니까 머리는 뱀 위치에 추가
        else:
            time += 1
            break
        time += 1
        # 여기서 회전
        if turn_index < l and turn[turn_index][0] == time: 
            dir = turn_dir(dir, turn[turn_index][1])
            turn_index += 1
    return time

print(solution())