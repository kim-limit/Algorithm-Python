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

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = [] # 비용 저장

# 최소비용으로 신장 트리 만듬
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(cost)
        
# 가장 큰 비용 삭제        
result.pop(-1)
print(sum(result))
