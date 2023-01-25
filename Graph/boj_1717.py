import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(100000)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [i for i in range(n + 1)] 

for _ in range(m):
    union, a, b = map(int, input().split())
    # 0이면 집합 합침
    if union == 0:
        union_parent(parent, a, b)
    # 1이면 부모가 같은지 확인 후 출력
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES\n')
        else:
            print('NO\n')