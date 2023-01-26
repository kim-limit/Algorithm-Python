def check(line):
    used = [False] * n
    for i in range(1, n):
        if abs(line[i] - line[i - 1]) > 1: # 차이 1 아니면 불가
            return False
        if line[i - 1] > line[i]: # 왼쪽이 더 크면 오른쪽에 경사로
            for j in range(l): # 경사로 길이만큼 생성
                if i + j >= n or used[i + j]: # 범위 벗어남
                    return False
                if line[i] != line[i + j]: # 연속 아니면
                    return False
                used[i + j] = True
        elif line[i - 1] < line[i]: # 오른쪽이 더 크면
            for j in range(l):
                if i - j - 1 < 0 or used[i - j - 1]:
                    return False
                if line[i - 1] != line[i - j - 1]:
                    return False
                used[i - j - 1] = True
    return True
n, l = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

result = 0
for i in range(n):
    if check(array[i]): # 가로 방향
        result += 1
    if check([array[j][i] for j in range(n)]): # 세로 방향
        result += 1
print(result)



