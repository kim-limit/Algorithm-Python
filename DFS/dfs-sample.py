def dfs(graph, v, visited):
    visited[v] = True  # 우선 방문 체크
    print(v, end=' ')
    for i in graph[v]:  # v번 노드가 인전한 애들 확인
        if not visited[i]:  # 만약 방문 안했으면 stack에 추가후 들어감 (작은거 부터)
            dfs(graph, i, visited)

graph = [  # 그래프 상태
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9  # 방문 상태 저장

dfs(graph, 1, visited)