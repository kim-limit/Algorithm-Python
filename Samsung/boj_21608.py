n = int(input())

# 입력값
array = []
for _ in range(n * n):
    array.append(list(map(int, input().split())))

# 학생 자리
graph = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for data in array:
    # 학생 번호
    student = data[0]
    # 정렬에 필요한 조건 저장
    info = []
    for x in range(n):
        for y in range(n):
            love = 0 # 좋아하는 사람 수
            blank = 0 # 빈칸 수
            # 이미 자리 있으면 넘김
            if graph[x][y] != 0:
                continue
            # 상하좌우 확인
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx >= n or nx < 0 or ny >= n or ny < 0:
                    continue
                if graph[nx][ny] in data[1:]:
                    love += 1
                if graph[nx][ny] == 0:
                    blank += 1
            info.append([love, blank, x, y])
    # 좋아하는 사람수, 빈칸 내림차순, 위치 오름차순
    info.sort(key = lambda x :(-x[0], -x[1], x[2], x[3]))
    graph[info[0][2]][info[0][3]] = student
    
array.sort() # 계산을 위해 정렬
result = 0
for x in range(n):
    for y in range(n):
        # 주변 좋아하는 사람 수
        good = 0
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if graph[nx][ny] in array[graph[x][y] - 1]:
                good += 1
        if good == 0:
            continue
        result += 10 ** (good - 1)

print(result)