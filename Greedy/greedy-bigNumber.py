# 입력
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 정렬
data.sort()

first = data[n-1]
second = data[n-2]

result = 0

# 내 코드
count = 0
for i in range(0, m): # m번 반복
    if(count == k): # k번 이상 되면 2번째 큰값 더함
        result += second
        count = 0
    else: # k번 전까지 가장 큰 값 더함
        result += first
        count += 1

# 이코테 풀이
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

# m이 1억이상이면 시간초과남 -> 수학적 계산
count = int(m / (k + 1)) * k # 반복되는 큰수의 집합 갯수
count += m % (k + 1) # 나머지 큰수 더해주기

result += (count) * first
result += (m - count) * second

#결과
print(result)