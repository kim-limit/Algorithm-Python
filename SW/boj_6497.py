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

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n)]
    edges = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    edges.sort()

    result = 0
    for cost, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
        else:
            result += cost

    print(result)