r, c, k = map(int, input().split())

array = []
for _ in range(3):
    array.append(list(map(int, input().split())))
    
def count(list): # 계산 함수
    count_list = []
    for i in list:
        if i == 0: # 0은 안셈
            continue
        if (i, list.count(i)) not in count_list: # 처음 세는것만
            count_list.append((i, list.count(i))) # 숫자와 개수
            
    count_list.sort(key=lambda x : (x[1], x[0])) # 우선순위를 개수먼저

    result = []
    for i in range(len(count_list)): 
        result.append(count_list[i][0])
        result.append(count_list[i][1])

    return result[:100] # 100개 까지만

def rc():
    global array
    tmp = [] # 결과 임시 저장
    max_value = -1 # 가장 긴 길이
    rows = len(array) # 행
    for i in range(rows):
        tmp.append(count(array[i]))
        if len(tmp[i]) > max_value:
            max_value = len(tmp[i])
    for i in range(rows): # 0으로 채움
        for j in range(max_value - len(tmp[i])):
            tmp[i].append(0)
    array = tmp # 기존 배열에 할당

answer = 0
while True:
    if r <= len(array) and c <= len(array[0]): # 범위 안에서만 체크
        if array[r - 1][c - 1] == k:
            break
    if answer == 100: # 100번째 넘어가면 끝냄
        answer = -1
        break
    rows = len(array) # 행
    cols = len(array[0]) # 열
    if rows >= cols:
        rc()
    else:
        array = list(zip(*array)) # 뒤집기
        rc()
        array = list(zip(*array))
    answer += 1
print(answer)