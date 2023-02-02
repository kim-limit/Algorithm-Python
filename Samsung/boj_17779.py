def solve(x, y, d1, d2):
    wall = [[0] * (n + 1) for _ in range(n + 1)] # 경계선
    wall[x][y] = -1
    for i in range(1, d1 + 1):
        wall[x + i][y - i] = -1
        wall[x + d2 + i][y + d2 - i] = -1
    for i in range(1, d2 + 1):
        wall[x + i][y + i] = -1
        wall[x + d1 + i][y - d1 + i] = -1
    
    area = [0] * 5
    # 1번
    for i in range(1, x + d1):
        for j in range(1, y + 1):
            if wall[i][j] == -1:
                break
            area[0] += array[i][j]
    # 2번
    for i in range(1, x + d2 + 1):
        for j in range(n, y, -1): # 오른쪽에서 왼쪽이라 -1
            if wall[i][j] == -1:
                break
            area[1] += array[i][j]
    # 3번
    for i in range(x + d1, n + 1):
        for j in range(1, y - d1 + d2):
            if wall[i][j] == -1:
                break
            area[2] += array[i][j]
    # 4번
    for i in range(x + d2 + 1, n + 1):
        for j in range(n, y - d1 + d2 - 1, -1): # 오른쪽에서 왼쪽이라 -1
            if wall[i][j] == -1:
                break
            area[3] += array[i][j]

    area[4] = total - sum(area)
    return max(area) - min(area)

n = int(input())

array = [[0] * (n + 1)]
for _ in range(n):
    array.append([0] + list(map(int, input().split())))
array.append([0] * (n + 1))

total = 0 # 전체 값
for i in range(1, n + 1):
    for j in range(1, n + 1):
        total += array[i][j]

result = int(1e9)

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if x + d1 + d2 > n:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > n:
                    continue
                result = min(result, solve(x, y, d1, d2))

print(result)