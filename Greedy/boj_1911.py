n, l = map(int, input().split())

sand = []
for i in range(n):
    start, end = map(int, input().split())
    sand.append([start, end])

## 제일 뒤부터로 정렬
sand.sort(key = lambda x:x[1], reverse=True)

count = 0
last_index = sand[0][1]

for start, end in sand:
    if last_index < start:
        continue
    if last_index < end: # 판의 길이가 넘어왔을때
        end = last_index
    len = end - start
    remain = len % 3
    if remain == 0:
        last_index = start
        count += len // 3
    else:
        last_index = start - 3 + remain
        count += len // 3 + 1
    print(last_index)

print(count)