n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
array.append([0,0])

for i in range(1, len(array)):
    max_value = 0
    for j in range(i):
        if  j + array[j][0] <= i: # 그전에 일 할 수 있는날
            max_value = max(array[j][1], max_value)
    
    array[i][1] += max_value
print(array[n][1])