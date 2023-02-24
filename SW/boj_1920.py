from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

arr.sort()
for i in find:
    index = bisect_left(arr, i)    
    if index < len(arr) and arr[index] == i:
        print(1)
    else:
        print(0)