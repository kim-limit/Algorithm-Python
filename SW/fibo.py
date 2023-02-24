def fibo(n):
    if n <= 1:
        return 1
    else:
        if(dp[n] > 0):
            return dp[n]
        dp[n] = fibo(n - 1) + fibo(n - 2)
        return dp[n]
        
n = 10
dp = [0] * 100
dp[1] = 1
dp[2] = 2
print(fibo(5))