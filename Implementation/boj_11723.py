import sys

m = int(sys.stdin.readline())

s = set()
for _ in range(m):
    cal = sys.stdin.readline().strip().split()
    if len(cal) == 1:
        if cal[0] == 'all':
            s = set([i for i in range(1, 21)]) 
        else:
            s = set()
        continue
    
    func, x = cal[0], cal[1]
    x = int(x)
    if func == 'add':
        s.add(x)
    elif func == 'remove':
        s.discard(x)
    elif func == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    elif func == 'toggle':
        if x in s:
            s.discard(x)
        else:
            s.add(x)