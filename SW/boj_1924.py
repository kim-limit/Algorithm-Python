x, y = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dotw = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
tmp = 0
for i in range(1, x):
    tmp += days[i] % 7

print(dotw[(tmp + y - 1) % 7])