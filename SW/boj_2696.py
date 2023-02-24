import heapq

def check():
    left, right = [], [] # 최소힙, 최대힙
    middle = arr[0] # 첫번째 값
    result = [middle]
    for i in range(1, len(arr)):
        if middle > arr[i]: # 작으면 left
            heapq.heappush(left, -arr[i])
        else: # 크거나 같으면 right
            heapq.heappush(right, arr[i])
        if i % 2 == 0: # 두번 하고 나면 중앙값 결정
            if len(left) > len(right): # left가 많으면 제일 큰거 뺌
                heapq.heappush(right, middle) # 중앙값 right에 넣어줌
                middle = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -middle)
                middle = heapq.heappop(right)
            result.append(middle)

    print(len(result))
    for i in range(len(result)):
        if (i + 1) != 1 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()

t = int(input())

for _ in range(t):
    m = int(input())
    arr = []
    if m % 10 == 0:
        for _ in range(m // 10):
            arr += list(map(int, input().split()))
    else:
        for _ in range(m // 10 + 1):
            arr += list(map(int, input().split()))
    check()