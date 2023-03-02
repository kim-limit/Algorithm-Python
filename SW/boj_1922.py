def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort() # 비용을 기준으로 정렬

result = 0 # 최소 비용
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b): # 사이클 x
        union_parent(parent, a, b)
        result += cost

print(result)