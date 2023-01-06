def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False
    
n = int(input())
parts = list(map(int, input().split()))
parts.sort()

m = int(input())
finds = list(map(int, input().split()))

for find in finds:
    if binary_search(parts, find, 0, len(parts) - 1):
        print('yes')
    else:
        print('no')