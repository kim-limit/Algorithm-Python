n = int(input())
x, y = 1, 1  # 시작점

moves = input().split()

#LRUD에 따라 좌표 이동 설정
dx = [0, 0, -1, 1] 
dy = [-1, 1, 0, 0]
types = ["L", "R", "U", "D"]

for move in moves:
    for i in range(4):
        if move == types[i]:  # 움직임 일치 시 nx, ny로 임시 위치 설정
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    # 조건 충족시 움직임
    x = nx
    y = ny

print(x, y)

