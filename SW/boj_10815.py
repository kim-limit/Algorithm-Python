from bisect import bisect_left
n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
find = list(map(int, input().split()))
for i in find:
    index = bisect_left(card, i)
    if index < len(card) and card[index] == i:
        print('1', end=' ')
    else:
        print('0', end=' ')