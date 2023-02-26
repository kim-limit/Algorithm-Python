def dfs(result, depth):
    global cnt
    if depth == n:
        cnt += 1
        return
    for i in range(n):
        if visited[i] == 0 and result + arr[i] - k >= 0:
            visited[i] = 1
            dfs(result + arr[i] - k, depth + 1)
            visited[i] = 0
n, k = map(int, input().split())

arr = list(map(int, input().split()))
visited = [0] * n
cnt = 0
dfs(0,0)
print(cnt)


