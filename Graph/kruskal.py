def find_parent(parent, x):
    # 가장 큰 부모 찾을 때 까지 재귀
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split()) # 노드와 간선의 개수
parent = [0] * (v + 1) # 부모 테이블

edges = [] # 간선 리스트
result = 0 # 간선 합

# 부모 테이블 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용순으로 정렬해야함

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클 없으면 합침
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)