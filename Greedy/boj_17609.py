# def checkIsSame(str1, str2): # 반나눴을때 같은지 확인하는 함수
#     if str1 == str2[::-1]:
#         return True

# def checkIsContain(str1, str2):
#     reversed = str2[::-1]
#     if str1 == reversed[1:]:
#         return True
#     for i in range(1, len(reversed)):
#         if str1 == reversed[0:i] + reversed[i+1:]:
#             return True
#     return False

# for i in range(t):
#     str = input()
#     # 홀수일때
#     if len(str) % 2 != 0: 
#         if checkIsSame(str[:len(str)//2], str[len(str)//2+1:]):
#             print(0) # 화문이면 0출력
#         else: # 화문 아니면 반잘라서 확인
#             if checkIsContain(str[:len(str)//2], str[len(str)//2:]):
#                 print(1)
#             elif checkIsContain(str[len(str)//2+1:], str[:len(str)//2+1]):
#                 print(1)
#             else:
#                 print(2)
#     else:
#         if checkIsSame(str[:len(str)//2], str[len(str)//2:]):
#             print(0) # 화문이면 0출력
#         else:
#             if checkIsSame(str[:len(str)//2 -1], str[len(str)//2+1:]):
#                 print(1)
#             else:
#                 print(2)

def finalCheck(str, left, right):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def checkIsSame(str, left, right):
    if str == str[::-1]: # 바로 화문인 경우
        return 0
    while left < right: # 1 or 2
        if str[left] == str[right]: # 같으면 한칸씩 이동
            left += 1
            right -= 1
        else:
            leftCheck = finalCheck(str, left + 1, right) # 왼쪽 한칸 건너뜀
            rightCheck = finalCheck(str, left, right-1) # 오른쪽 한칸 건너뜀
            if leftCheck or rightCheck: # 다른 문자 안나왔으면 회문임
                return 1
            else: # 다른 문자 나온 경우
                return 2
    return 1
    
t = int(input())

for i in range(t):
    str = input()
    print(checkIsSame(str, 0, len(str)-1))

    