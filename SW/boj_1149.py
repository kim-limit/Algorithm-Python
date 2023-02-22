n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for house in range(1, n): # 집
    graph[house][0] = min(graph[house - 1][1], graph[house - 1][2]) + graph[house][0]    
    graph[house][1] = min(graph[house - 1][0], graph[house - 1][2]) + graph[house][1]    
    graph[house][2] = min(graph[house - 1][0], graph[house - 1][1]) + graph[house][2]    
    
print(min(graph[n - 1]))