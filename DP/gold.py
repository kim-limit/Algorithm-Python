t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    for i in range(1, m):
        for j in range(n):
            left_up, left, left_down = 0, 0, 0
            if j == 0: # 왼쪽 위 없는 경우
                left = array[i + j * m - 1]
                left_down = array[i + j * m - 1 + m]
            elif j == n -1: # 왼쪽 아래 없는 경우
                left = array[i + j * m - 1]
                left_up = array[i + j * m - 1 - m]
            else:
                left_up = array[i + j * m - 1 - m]
                left = array[i + j * m - 1]
                left_down = array[i + j * m - 1 + m]
            # 왼쪽 위, 왼쪽, 왼쪽 아래 중 가장 큰값에 자기 더하기
            array[i + j * m] = max(left_up, left, left_down) + array[i + j * m]

    result = -1
    # 마지막줄에서 가장 큰값 출력
    for i in range(n):
        result = max(result, array[m - 1 +  i * m])
    print(result)