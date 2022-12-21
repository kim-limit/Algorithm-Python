n, k = map(int, input().split())

result = 0

# 반복문
while True:
    if n == 1:
        break
    if n % k == 0:
        n //= k
    else: 
        n -= 1
    result += 1

# 최대 배수로 만든뒤 계산
while True:
    # 최대 배수 만든후 n - target하면 1씩 뺀 횟수
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

# 마무리로 1로 만들기
result += (n - 1)

print(result)