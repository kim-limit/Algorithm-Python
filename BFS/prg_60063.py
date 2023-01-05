from collections import deque

def get_next_index(index, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    next_index = []
    index = list(index)
    x1, y1, x2, y2 = index[0][0], index[0][1], index[1][0], index[1][1]
    for dir in range(4):
        nx1 = x1 + dx[dir]
        ny1 = y1 + dy[dir]
        nx2 = x2 + dx[dir]
        ny2 = y2 + dy[dir]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_index.append({(nx1, ny1), (nx2, ny2)})
    # 가로일때 회전 가능한지
    if x1 == x2:
        for i in [-1, 1]:
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_index.append({(x1, y1), (x1 + i, y1)})
                next_index.append({(x2, y2), (x2 + i, y2)})
    # 세로일 때
    elif y1 == y2:
        for i in [-1, 1]:
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_index.append({(x1, y1), (x1, y1 + i)})
                next_index.append({(x2, y2), (x2, y2 + i)})
    # print(next_index)
    return next_index



def bfs(board, n):
    index = {(1, 1), (1, 2)}
    queue = deque()
    queue.append((index, 0))
    visited = []
    visited.append(index)
    while queue:
        index,  cost = queue.popleft()
        if (n, n) in index:
            return cost
        
        for next_index in get_next_index(index, board):
            if next_index not in visited:
                queue.append((next_index, cost + 1))
                visited.append(next_index)
    return 0

def solution(board):
    answer = 0
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    return bfs(new_board, n)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))