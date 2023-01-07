def binary_search(array, start, end, target, lens):
    result = 0
    while start <= end:
        mid = (start + end) // 2 # 공유기 사이의 거리 나타냄
        count = 1
        value = array[0]
        for i in range(1, lens):
            if array[i] >= value + mid:
                count += 1
                value = array[i]
        if count >= target:
            start = mid + 1
            result  = mid
        else:
            end = mid -1
    return result

n, c = map(int ,input().split())

data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
start = 1
end = data[-1] - data[0]
print(binary_search(data, start, end, c, n))