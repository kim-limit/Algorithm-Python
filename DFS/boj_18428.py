n = int(input())

graph = []
for i in range(n):
    graph.append(list(input().split()))

result = "NO"

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def isSafe():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "T": # 선생님위치 찾은후 감시 시작
                for dir in range(4):
                    nx = i
                    ny = j
                    while True: # 상하좌우 끝까지 확인
                        nx += dx[dir]
                        ny += dy[dir]
                        if nx >= n or nx < 0 or ny >= n or ny < 0: # 인덱스 값 넘어가면 다른방향 감시
                            break
                        if graph[nx][ny] == "S": # 학생 발견하면 false return
                            return False
                        if graph[nx][ny] == "O": # 벽 발견하면 다른 방향 감시
                            break
    return True # 감시 다 피한경우 true 반환

def dfs(count): # 장애물 세우기
    global result
    if count == 3: # 장애물 3개 세웠을때 안전한지 체크
        if isSafe():
            result = "YES"
        return
    for i in range(n): 
        for j in range(n):
            if graph[i][j] == "X": # 빈곳이면 장애물 세우기
                graph[i][j] = "O"
                count += 1
                dfs(count)
                graph[i][j] = "X"
                count -= 1


dfs(0)
print(result)

# 조합으로 풀어도 됨