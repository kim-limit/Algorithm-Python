n = int(input())
m = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

graph = [[int(1e9)] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
        elif arr[i][j] == 1:
            graph[i][j] = 1

travel = list(map(int, input().split()))
for k in range(n):
    for i in range(n):
        for j in range(n):
            if k == i: 
                continue 
            if i == j:
                continue
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])


result = 'YES'
for i in range(m - 1):
    if graph[travel[i] - 1][travel[i + 1] - 1] == int(1e9):
        result = 'NO'

print(result)