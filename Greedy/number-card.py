n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) # 각 행별로 가장 작은수

    result = max(min_value, result) # 현재 까지 구한 값중 가장 큰거 설정

print(result)