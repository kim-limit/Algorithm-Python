import heapq

def solution(food_times, k):
    answer = 0
    
    if sum(food_times) <= k:
        return -1

    food_len = len(food_times)

    hq = []
    for i in range(0, len(food_times)):  # 우선 순위 큐에 [음식 길이, 음식 번호]로 삽입
        heapq.heappush(hq, [food_times[i], i + 1])

    sum_foods = 0
    prev_foods = 0
    while True:
        if hq[0][0] == sum_foods:
            heapq.heappop(hq)
            food_len -= 1
            continue
        if (hq[0][0] - sum_foods) * food_len > k : # 만약 음식 하나 다 못먹는 경우
            break

        min_len = heapq.heappop(hq)[0] - sum_foods
        k -= (min_len * food_len)
        sum_foods += min_len
        food_len -= 1
        print(min_len)
    result = sorted(hq, key=lambda x: x[1])
    answer = result[k % food_len][1]
    return answer

print(solution([3, 1, 2],5))