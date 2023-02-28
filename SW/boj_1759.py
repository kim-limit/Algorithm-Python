from itertools import combinations

l, c = map(int, input().split())

alpha_list = list(input().split())
str_list = combinations(alpha_list, l)
result = []
for i in str_list:
    tmp = list(i)
    cnt = 0
    for j in ['a', 'e', 'i', 'o', 'u']:
        if j in tmp:
            cnt += 1
    if l - cnt > 1 and cnt > 0:
        tmp.sort()
        result.append(tmp)

result.sort()
for i in result:
    print("".join(i))