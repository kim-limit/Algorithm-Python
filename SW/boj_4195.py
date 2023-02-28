def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b, number):
    a = find_parent(parent, a) # 루트 노드 찾음
    b = find_parent(parent, b) 
    if a < b:
        parent[b] = a
        number[a] += number[b] # 루트 노드에 작은애의 루트노드 값 더해줍
    elif a > b: # 같은 친구인 경우가 나오면 안되니까 == 제외
        parent[a] = b
        number[b] += number[a]

t = int(input())

for _ in range(t):
    f = int(input())
    parent = [i for i in range(f * 2)]
    friend = {} # 이름에 따른 index 저장
    number = [0] * (f * 2) # 루트 노드에 친구수 정해줄거임
    index = 0
    for i in range(f):
        a, b = input().split()
        if a not in friend.keys(): # 이미 안나왔던거면 초기화
            friend[a] = index
            number[friend[a]] = 1
            index += 1
        if b not in friend.keys():
            friend[b] = index
            number[friend[b]] = 1
            index += 1
        # union
        union_parent(parent, friend[a], friend[b], number) # a, b 합침
        print(number[find_parent(parent, friend[a])]) # a또는 b의 루트노드의 수 출력
