location = input()

x = ord(location[0]) - ord("a") + 1
y = int(location[1])
count = 0

moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    if(nx < 1 or nx > 8 or ny < 1 or ny > 8):
        continue
    count+=1

print(count)