n = int(input())
express = list(input())

num = []
for _ in range(n):
    num.append(int(input()))

for i in range(len(express)): # 알파벳에 맞게 할당
    index = ord(express[i]) - ord('A')
    if 0 <= index <= 26:
        express[i] = num[index]

cal = []
for s in express:
    if s == "*":
        first = cal.pop()
        second = cal.pop()
        cal.append(first * second)
    elif s == '+':
        first = cal.pop()
        second = cal.pop()
        cal.append(first + second)
    elif s == '-':
        first = cal.pop()
        second = cal.pop()
        cal.append(second - first)
    elif s == '/':
        first = cal.pop()
        second = cal.pop()
        cal.append(second / first)
    else:
        cal.append(s)

print("{:.2f}".format(cal[0]))