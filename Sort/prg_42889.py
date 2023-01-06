def solution(N, stages):
    stages.sort()
    fail_ratio = []
    for stage in range(1, N + 1):
        fail = 0
        lens = 0
        for i in stages:
            if stage == i:
                fail += 1
            if stage <= i:
                lens += 1
        if lens == 0:
            fail_ratio.append([stage, 0])
        else:
            fail_ratio.append([stage, fail/lens])
    fail_ratio.sort(key = lambda a: -a[1])

    answer = [x[0] for x in fail_ratio]
    return answer

print(solution(5,[2, 2, 2, 2, 2, 2, 2, 2]))
