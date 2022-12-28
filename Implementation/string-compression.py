def solution(s):
    
    if(len(s) == 1):
        return 1
    minStr = 1001
    for j in range(1, len(s) // 2 + 1):
        count = 1
        prev = ""
        result = []
        for i in range(0, len(s), j):
            if s[i:i+j] == prev:
                count += 1
            else:
                if count > 1:
                    result.append(str(count))
                    result.append(prev)
                else:
                    result.append(prev)
                count = 1
            prev = s[i:i+j]
        if count > 1:
            result.append(str(count))
            result.append(prev)
        else:
            result.append(prev)
        minStr = min(minStr, len("".join(result)))
        

    return minStr