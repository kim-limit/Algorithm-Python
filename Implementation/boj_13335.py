from collections import deque
n, w, l = map(int, input().split())

array = list(map(int, input().split()))

cnt = 1 # 시간
q = deque([0]*(w-1)) # 0으로 채우고 첫번째 차 넣음
q.append(array[0])
i = 1 # 차의 인덱스

while q:
    if i == n: # 마지막 차 들어가면 다 빼줌
        cnt += w
        break
    cnt += 1 
    q.popleft() # 맨 앞차 뺴고
    if array[i] + sum(q) > l: # 차 못들어가면 0
        q.append(0)
    else: # 차 들어가면 차 넣음
        q.append(array[i])
        i += 1
    
print(cnt)