def find_parent(parent, x):
    # 가장 큰 부모 찾을 때 까지 재귀
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

v, e = map(int, input().split()) # 노드와 간선의 개수
parent = [0] * (v + 1) # 부모 테이블

# 부모 테이블 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 유무
# union 연산
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    union_parent(parent, a, b)

if cycle:
    print('사이클 발생')
else:
    print('사이클 없음')