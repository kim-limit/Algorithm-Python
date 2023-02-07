from collections import deque

r, c, n = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                for dir in range(4):
                    nx = i + dx[dir]
                    ny = j + dy[dir]
                    if nx >= r or nx < 0 or ny >= c or ny < 0:
                        continue
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = 'x'
                graph[i][j] = 'x'
            else:
                if graph[i][j] != 'x':
                    graph[i][j] = '.'
def reverse():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'x':
                graph[i][j] = '.'
            else:
                graph[i][j] = 'O'

# 짝수면 0
# 홀수면 폭탄 터트림 돌려서
if n % 2 == 0:
    for i in range(r):
        for j in range(c):
            print('O', end="")
        print()
else:
    for i in range(n // 2):
        bomb()
        reverse()
    for i in range(r):
        for j in range(c):
            print(graph[i][j], end="")
        print()