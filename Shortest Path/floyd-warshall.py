INF = int(1e9)

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 경우는 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선에 대한 정보로 테이블 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 노드 1부터 n 까지 확인
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
# 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end =' ')
        else:
            print(graph[a][b], end = ' ')
    print()