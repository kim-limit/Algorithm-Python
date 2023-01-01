from itertools import combinations

def get_sum(chicken, home):
    result = 0
    for x, y in home:
        min_len = 100
        for nx, ny in chicken:
            lens = abs(x - nx) + abs(y - ny)
            min_len = min(min_len, lens)
        result += min_len
    return result

def solution():
    n, m = map(int , input().split())

    maps = []
    chicken = []
    home = []
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(len(arr)):
            if arr[j] == 2:
                chicken.append([i,j])
            elif arr[j] == 1:
                home.append([i, j])
        maps.append(arr)

    # 조합으로 m개의 치킨집 구합
    new_chicken = list(combinations(chicken, m))
    min_result = 10000
    for i in range(len(new_chicken)):
        result = get_sum(new_chicken[i], home)
        min_result = min(min_result, result)

    return min_result

print(solution())
