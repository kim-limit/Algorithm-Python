def solution(s):
    
    if(len(s) == 1): # 만약 문자 길이가 1이면 바로 1로 return
        return 1
    minStr = 1001 # 최대 길이가 1000임
    for j in range(1, len(s) // 2 + 1): # 몇개씩 묶을건지 정함
        count = 1 # 연속된 문자 갯수
        prev = "" # 이전 문자
        result = [] # 결과 배열
        for i in range(0, len(s), j):
            if s[i:i+j] == prev: # 이전 문자와 같으면 추가하지 않고 갯수만 +
                count += 1
            else: # 이전 문자와 다를때
                if count > 1: # 만약 2개이상 연속되었을때
                    result.append(str(count))
                    result.append(prev)
                else: # 처음 나온 문자일 때
                    result.append(prev)
                count = 1
            prev = s[i:i+j]
        # 마지막 문자열 추가    
        if count > 1:
            result.append(str(count))
            result.append(prev)
        else:
            result.append(prev)
        minStr = min(minStr, len("".join(result)))
        

    return minStr