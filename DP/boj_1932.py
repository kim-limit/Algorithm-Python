n = int(input())

prev_array = []
prev_array.append(int(input())) # 삼각형 제일 위

for _ in range(n - 1): 
    array = list(map(int, input().split()))
    lens = len(array)
    for i in range(lens):
        if i == 0: # 맨 왼쪽
            array[i] = array[i] + prev_array[i]
        elif i == lens - 1: # 맨 오른쪽
            array[i] = array[i] + prev_array[i - 1]
        else: # 중간 쪽
            array[i] = array[i] + max(prev_array[i - 1], prev_array[i])
    prev_array = array
# 마지막줄에서 가장 큰 값 출력
print(max(prev_array))