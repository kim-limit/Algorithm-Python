from collections import deque

n, k = map(int, input().split())

graph = []
for _ in range(n): 
    graph.append(list(map(int, input().split())))

horses = [] # 말 정보 (번호, x, y, 방향)
maps = [[deque() for _ in range(n)] for _ in range(n)] # 맵에서 말의 상태
for i in range(k):
    x, y, dir = map(int, input().split())
    horses.append((x - 1, y - 1, dir, i))
    maps[x - 1][y - 1].append(i)

    
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
while True:
    for horse in horses:
        if maps[horse[0]][horse[1]][0] != horse[3]:
            continue
        nx = horse[0] + dx[horse[2]]
        ny = horse[1] + dy[horse[2]]
        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue
        if graph[nx][ny] == 0: # 흰색일 때
            continue
        




