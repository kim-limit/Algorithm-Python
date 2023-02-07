h, w, x, y = map(int, input().split())

graph = []
for _ in range(h + x):
    graph.append(list(map(int, input().split())))

for i in range(h - x):
    for j in range(w - y):
        graph[i + x][j + y] -= graph[i][j]

for i in range(h):
    for j in range(w):
        print(graph[i][j], end=" ")
    print()