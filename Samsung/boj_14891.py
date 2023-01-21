gear =[]
for _ in range(4):
    gear.append(list(map(int, input())))

k = int(input())

moves = []
for _ in range(k):
    moves.append(list(map(int, input().split())))
# 맞닿음 2, 6
for n, dir in moves:
    # 시계 돌면 1 반대 -1 안돌면 0
    move = [0, 0, 0, 0]
    if n == 1:
        move[0] = dir
        if gear[0][2] != gear[1][6]:
            move[1] = move[0] * -1
        else:
            move[1] = 0
        if gear[1][2] != gear[2][6]:
            move[2] = move[1] * -1
        else:
            move[2] = 0
        if gear[2][2] != gear[3][6]:
            move[3] = move[2] * -1
        else:
            move[3] = 0
    elif n == 2:
        move[1] = dir
        if gear[0][2] != gear[1][6]:
            move[0] = move[1] * -1
        else:
            move[0] = 0
        if gear[1][2] != gear[2][6]:
            move[2] = move[1] * -1
        else:
            move[2] = 0
        if gear[2][2] != gear[3][6]:
            move[3] = move[2] * -1
        else:
            move[3] = 0
    elif n == 3:
        move[2] = dir
        if gear[2][2] != gear[3][6]:
            move[3] = move[2] * -1
        else:
            move[3] = 0
        if gear[1][2] != gear[2][6]:
            move[1] = move[2] * -1
        else:
            move[1] = 0
        if gear[0][2] != gear[1][6]:
            move[0] = move[1] * -1
        else:
            move[0] = 0
    elif n == 4:
        move[3] = dir
        if gear[2][2] != gear[3][6]:
            move[2] = move[3] * -1
        else:
            move[2] = 0
        if gear[1][2] != gear[2][6]:
            move[1] = move[2] * -1
        else:
            move[1] = 0
        if gear[0][2] != gear[1][6]:
            move[0] = move[1] * -1
        else:
            move[0] = 0
    # 움직이기
    for i in range(len(move)):
        if move[i] == 0:
            continue
        elif move[i] == 1:
            temp = gear[i].pop(-1)
            gear[i].insert(0, temp)
        else:
            temp = gear[i].pop(0)
            gear[i].append(temp)
# 결과 
sum = 0
for i in range(4):
    if gear[i][0] == 0:
        continue
    sum += 2 ** i
    
print(sum)