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

parent = [i for i in range(n)]
result = -1
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split()))) 

for i in range(m):
    a, b = arr[i]
    print(parent)
    if find_parent(parent, a) == find_parent(parent, b):
        result = i + 1
        break
    union_parent(parent, a, b)

if result == -1:
    print(0)
else:
    print(result)