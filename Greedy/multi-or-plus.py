s = list(input())

result = int(s[0])
for n in range(1, len(s)):
    # 0, 1은 곱하는 거 보다 더하는게 더 큼
    num = int(s[n])
    if result > 1:
        result *= num
    else:
        result += num
    
print(result)