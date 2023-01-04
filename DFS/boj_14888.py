n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def solution(i, result):
    global add, sub, mul, div, min_value, max_value
    # 계산 마지막
    if i == n:
        min_value = min(min_value, result)
        max_value = max(max_value, result)
    # 계산 중
    else:
        if add > 0:
            add -= 1
            solution(i + 1, result + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            solution(i + 1, result - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            solution(i + 1, result * num[i])
            mul += 1
        if div > 0:
            div -= 1
            solution(i + 1, int(result / num[i]))
            div += 1

solution(1, num[0])
    
print(max_value)
print(min_value)