n = input()

dp = [0] * 5001
result = 0

def fibo():
    if n == '0':
        return False
    dp[0] = 1
    if len(n) == 1:
        return True
    if 1 <= int(n[:2]) <= 26 and n[1] != '0':
        dp[1] = 2
    else:
        dp[1] = 1
    if n[1] == '0' and 3 <= int(n[0]):
        return False
    for i in range(2, len(n)):
        if n[i] == '0':
            if n[i - 1] != '1' and n[i - 1] != '2':
                return False
            dp[i] = dp[i - 2]
        else:
            if 1 <= int(n[i - 1] + n[i]) <= 26:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
    return True

if fibo():
    print(dp[len(n) - 1] % 1000000) 
else:
    print(0)