from bisect import bisect_left

n = int(input())
array = list(map(int, input().split()))

dp = [1] * n # 우선순위 저장할 배열 
cp = [array[0]] # 이진 탐색을 위한 배열

for i in range(1, n):
    if array[i] > cp[-1]:
        cp.append(array[i])
        dp[i] = len(cp) # 이진 탐색 배열의 길이가 큰 수의 순위와 같음
    else:
        index = bisect_left(cp, array[i]) # 이진 탐색으로 가장 가까운 큰 수랑 바꿔줌
        cp[index] = array[i] 
        dp[i] = index + 1 # 바꾼 위치와 우선순위 같아짐

max_value = max(dp) # 가장 큰 우선순위 = 배열의 개수
print(max_value)

result = []
for i in range(n - 1, -1, -1): # 우선 순위 역순으로 출력
    if dp[i] == max_value:
        result.append(array[i])
        max_value -= 1

result.reverse()
print(*result)