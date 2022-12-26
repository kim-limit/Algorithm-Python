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
    if last_index < start: # 이미 판자가 덮은 경우
        continue
    if last_index < end: # 판의 길이가 넘어왔을때
        end = last_index
    len = end - start
    remain = len % l
    if remain == 0: # 판자로 정확히 덮을 수 있는 경우
        last_index = start
        count += len // l
    else: # 판자가 남는경우
        last_index = start - l + remain
        count += len // l + 1

print(count)