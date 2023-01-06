n = int(input())
parts = list(map(int, input().split()))
parts.sort()

m = int(input())
finds = list(map(int, input().split()))

for find in finds:
    if find in parts:
        print('yes')
    else:
        print('no')