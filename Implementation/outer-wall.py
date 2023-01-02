from itertools import permutations

def solution(n, weak, dist):
    lens = len(weak)  # 확인해야 하는 취약 갯수

    for i in range(lens): # 원형이니까 두배길이로 늘려서 확인함
        weak.append(n + weak[i])

    friends = list(permutations(dist, len(dist)))
    min_friend = 1000
    for start in range(lens): # 시작지점을 취약지점중 1개씩 다 돌림
        for friend in friends: # 친구들의 순서만 바꿔서 모든 경우의수 다돌림
            count = 1 
            position = weak[start] + friend[count - 1] # 첫번쨰 친구가 외벽 검사하고 난뒤 마지막 위치
            for success in range(start, start + lens): # 취약지역을 검사했는지 확인
                if position < weak[success]: # 마지막 위치가 취약지역의 위치보다 밑에 있으면 확인 못한것 -> 친구 한명 더부름
                    count += 1
                    if count > len(dist): # 친구 다부른 경우
                        break
                    position =  weak[success] + friend[count - 1] # 부른 친구가 검사하고 난뒤 마지막 위치
            # 과정 반복
            min_friend = min(min_friend, count)

    if min_friend > len(dist):
        return -1
    return min_friend

print(solution(12, [1, 3, 4, 9, 10]	, [3, 5, 7]))