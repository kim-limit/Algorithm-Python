n = int(input())

swich = [-1] + list(map(int, input().split())) + [-1]

t = int(input())

def man(num):
    i = 1
    while num * i <= n: # 배수 변경
        swich[num * i] = abs(swich[num * i] - 1)
        i += 1

def woman(num):
    left = num - 1
    right = num + 1
    while swich[left] == swich[right] and swich[left] != -1 and swich[right] != -1: # 다른 경우 나올 떄 까지
        left -= 1
        right += 1

    # 변경
    swich[num] = abs(swich[num] - 1)
    for i in range(num - 1, left, -1):
        swich[i] = abs(swich[i] - 1)
    for i in range(num + 1, right):
        swich[ i] = abs(swich[i] - 1)

for _ in range(t):
    sex, num = map(int, input().split())
    if sex == 1: # 남자일 떄
        man(num)
    else: # 여자일 때
        woman(num)

for i in range(1, n+1):
    print(swich[i], end=" ")
    if i % 20 == 0:
        print()
