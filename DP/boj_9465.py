t = int(input())

for _ in range(t):
    n = int(input())

    array = []
    for _ in range(2):
        array.append(list(map(int, input().split())))

    # n이 1인경우 인덱스 에러나기 때문에 for문안에 넣었음
    for i in range(1, n):
        if i == 1:
            array[0][i] += array[1][i - 1]
            array[1][i] += array[0][i - 1]
        else:
            array[0][i] = max(array[1][i - 1], array[1][i - 2]) + array[0][i]
            array[1][i] = max(array[0][i - 1], array[0][i - 2]) + array[1][i]
    print(max(max(array[0]), max(array[1])))