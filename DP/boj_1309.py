n = int(input())

full = 2 # 전 줄에 사자가 있는 경우
empty = 1 # 전 줄에 사자가 없는 경우
result = 3 # 결과
for i in range(1, n):
    full = full + empty * 2
    empty = result
    result = full + empty

print(result % 9901)