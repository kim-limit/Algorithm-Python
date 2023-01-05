n, k = map(int ,input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

result = 0
for i in range(k):
    if a[i] < b[i]:
        result += b[i]
    else:
        result += a[i]
for i in range(k, len(a)):
    result += a[i]
print(result)