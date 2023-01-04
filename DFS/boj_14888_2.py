from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

# 리스트에 연산자 다 넣음
cal_list = []
for i in range(add):
    cal_list.append("+")
for i in range(sub):
    cal_list.append("-")
for i in range(mul):
    cal_list.append("*")
for i in range(div):
    cal_list.append("/")

# n-1개로 조합 다 만듬
cals = list(permutations(cal_list, (n-1)))

# 조합별로 계산
for cal in cals:
    result = num[0]
    for i in range(1, len(num)):
        if cal[i - 1] == "+":
            result += num[i]
        elif cal[i - 1] == "-":
            result -= num[i]
        elif cal[i - 1] == "*":
            result *= num[i]
        else:
            result = int(result / num[i])
    min_value = min(min_value, result)
    max_value = max(max_value, result)

print(max_value)
print(min_value)