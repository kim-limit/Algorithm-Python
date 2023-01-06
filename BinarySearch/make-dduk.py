def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        print(mid)
        if cut(array, mid) < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result
def cut(array, lens):
    sum_value = 0
    for i in array:
        if i > lens:
            sum_value += i - lens
    return sum_value
n, m = map(int, input().split())
dduk = list(map(int, input().split()))

print(binary_search(dduk, m, 0, max(dduk)))