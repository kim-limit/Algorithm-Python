from itertools import permutations

def solution(n, weak, dist):
    lens = len(weak)  # 확인해야 하는 취약 갯수

    for i in range(lens): # 원형이니까 두배길이로 늘려서 확인함
        weak.append(n + weak[i])

    friends = list(permutations(dist, len(dist)))
    min_friend = 1000
    for start in range(lens): # weak index를 기준으로 시작
        for friend in friends: # 친구 조합
            count = 1
            position = weak[start] + friend[count - 1] # 친구가 외벽 검사하고 난 뒤의 위치
            for success in range(start, start + lens): # 취약지역 검사
                if position < weak[success]:
                    count += 1
                    if count > len(dist):
                        break
                    position =  weak[success] + friend[count - 1]
            min_friend = min(min_friend, count)

    if min_friend > lens:
        return -1
    return min_friend

print(solution(12, [1, 3, 4, 9, 10]	, [3, 5, 7]))