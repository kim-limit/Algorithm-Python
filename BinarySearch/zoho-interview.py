def left_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid == 0 and array[mid] != target: # 못찾았을 경우 -1 반환
            return -1
        elif array[mid - 1] < target and array[mid] == target: # 찾았을 때 왼쪽에 더이상 없으면 반환
            return mid
        elif array[mid] >= target: # 완쪽에 더 있으면 왼쪽으로 이동
            end = mid - 1
        else:
            start = mid + 1
    return -1

def right_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid == n - 1 and array[mid] != target: # 못찾았을 경우 -1 반환
            return -1
        elif array[mid + 1] > target and array[mid] == target: # 찾았을 때 오른쪽에 더이상  없으면 반환
            return mid
        elif array[mid] > target: 
            end = mid - 1
        else: # 오른쪽에 더있으면 오른쪽으로 이동
            start = mid + 1
    return -1

def count_num(array, target, n):
    left = left_search(array, target, 0, n - 1)
    right = right_search(array, target, 0, n - 1)
    if left == -1:  # 하나라도 못찾으면 -1 반환
        return -1
    return right - left + 1


n, x = map(int, input().split())
data = list(map(int, input().split()))

print(count_num(data, x, n))