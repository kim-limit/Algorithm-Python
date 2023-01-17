n, m = map(int, input().split())
r, c, d = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 빈칸 0 벽 1 청소 2
# 북0, 동1, 남2, 서3
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def simul(r, c, d):
    result = 0
    while True:
        # 1번
        array[r][c] = 2
        result += 1
        count = 0 # 2-3
        # 2번
        while True:
            nd = (d - 1) % 4 # 왼쪽으로 회전
            nr = r + dr[nd] # 전진
            nc = c + dc[nd]
            if array[nr][nc] == 0: # 2-1
                d = nd
                r = nr
                c = nc
                break
            else: # 2-2
                d = nd
                count += 1

            if count == 4: # 2-3
                nr = r - dr[d] # 후진
                nc = c - dc[d]
                if array[nr][nc] == 1: # 2-4
                    return result
                r = nr
                c = nc
                count = 0
            
print(simul(r, c, d))