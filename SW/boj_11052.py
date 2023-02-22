n = int(input())

p = [0] + list(map(int, input().split()))

result = -1
for i in range(2, n + 1):
    for j in range(1, i // 2 + 1):
        p[i] = max(p[i], p[j] + p[i - j])

print(p[n])