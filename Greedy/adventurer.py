n = int(input())

adventurer = list(map(int,input().split()))

adventurer.sort()

# guild = []
guild = 0 # 한 길드 인원
count = 0 # 길드의 수
for i in adventurer:
    guild += 1 # 길드에 추가
    if guild >= i: # 길드인원보다 공포도 크면 다음 길드로 넘어감
        count += 1
        guild = 0
    # guild.append(i)
    # if len(guild) >= i:
    #     guild = []
    #     count += 1

print(count)

## 배열에 넣는 거 보다 그냥 숫자만 더하는게 빠르다!