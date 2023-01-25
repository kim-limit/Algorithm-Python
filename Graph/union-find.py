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

# union 연산
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 출력 하면서 큰 부모로 다시 초기화 됨
print('각 원소가 속한 집합: ', end = '')
for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')

print()

print('부모 테이블 : ', end = '')
for i in range(1, v + 1):
    print(parent[i], end = ' ')