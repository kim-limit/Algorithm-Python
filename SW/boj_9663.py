n = int(input())

queen = [0] * n
result = 0

def check(row): # 검사
    for i in range(row):
        # 대각선에 있는지, 위에 있는지 검사
        if abs(queen[row] - queen[i]) == row - i or queen[i] == queen[row]: 
            return False
    return True

def dfs(row):
    global result
    if row == n:
        result += 1
        return
    else:
        for i in range(n):
            queen[row] = i
            if check(row):
                dfs(row + 1)

dfs(0)
print(result)