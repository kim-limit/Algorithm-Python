from collections import defaultdict

def get_case(pizza, lens): # 피자 종류에 따라 만들 수 있는 경우의 수 반환
    return_case = defaultdict(int) # 다 0으로 초기화 되있음
    for i in range(lens):
        nums = pizza[i:] + pizza[:i] # 원형으로 만듬
        tmp = 0
        for num in nums:
            tmp += num
            return_case[tmp] += 1
            
    return_case[sum(pizza)] = 1 # 위의 과정 하면 다 더한 경우의 수가 lens개 생김 -> 1로 초기화
    return_case[0] = 1 # case[t]와 계산하기 위해서

    return return_case

t = int(input())
n, m = map(int, input().split())

pizza_a = []
pizza_b = []

for i in range(n):
    pizza_a.append(int(input()))
for i in range(m):
    pizza_b.append(int(input()))

case_a = get_case(pizza_a, n)
case_b = get_case(pizza_b, m)

result = 0
for i in range(t + 1):
    result += case_a[i] * case_b[t - i] 

print(result)