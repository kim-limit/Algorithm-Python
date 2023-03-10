from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    print(left_index, right_index)
    return right_index - left_index

n, x = map(int, input().split())
data = list(map(int, input().split()))

count = count_by_range(data, x , x)

if count == 0:
    print(-1)
else:
    print(count)