n, m = map(int, input().split())

ball = list(map(int, input().split()))

# 볼링공 무게에 따라 개수 나누기
weight = [ 0 * i for i in range(11)]

for i in ball:
    weight[i] += 1

result = 0
for i in range(1, m + 1):
    n -= weight[i] # 선택한 볼링공 무게 제외 개수
    result += n * weight[i] # 선택한 볼링공 무게와 나머지 개수 곱하기
print(result)