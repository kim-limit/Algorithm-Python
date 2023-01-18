n = list(map(int,input()))

lens = len(n)
dp = [0] * (lens + 1)

# 맨 앞이 0이면 불가능
if n[0] == 0:
    print("0")
else :
    # dp를 위해 앞에 하나 추가
    n = [0] + n
    # 0번과 1번은 무조건 1
    dp[0] = 1
    dp[1] = 1

    for i in range(2, lens + 1):
        # 0보다 크면, 0이 아니면 1칸 전 그대로 감
        if n[i] > 0:
            dp[i] += dp[i - 1]
        temp = n[i - 1] * 10 + n[i]
        # 두개로 쪼갤 수 있으면 2칸 전도 더함
        if temp >= 10 and temp <= 26 :
            dp[i] += dp[i - 2]
    # 결과 출력
    print(dp[lens] % 1000000)