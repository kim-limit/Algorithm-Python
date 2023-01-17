import math
n = int(input())

array = list(map(int, input().split()))

b, c = map(int, input().split())

count = 0
for i in array:
    last = i - b
    if last > 0:
        count += math.ceil(last / c)
    count += 1
print(count)