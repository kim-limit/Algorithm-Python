def isBalance(a): # 균형 문자열 확인
    return a.count('(') == a.count(')')

def isCorrect(a): # 올바른 문자열인지
    stack = []
    for i in a:
        if len(stack) == 0:
            stack.append(i)
        else:
            # 맨앞이 ")" 이면 문자열이 올바를 수 없음 -> ")"로 stack의 "("을 지워야함
            if i == ")" and stack[len(stack) - 1] == "(":
                stack.pop()
            else:
                stack.append(i)

    return len(stack) == 0
    # 앞뒤 버리고 문자열 뒤집기 (앞뒤를 뒤집는게 아니라 "(" <-> ")" 임)
def reverse(a):
    newStr = ""
    for i in range(1, len(a) - 1):
        if a[i] == ")":
            newStr += "("
        else:
            newStr += ")"
    return newStr

def solution(p):
    answer = ""
    # 빈 문자열 이면 "" return
    if p == '' or isCorrect(p):
        return p
    # u, v 나누는 과정
    for i in range(0, len(p), 2):
        if isBalance(p[:i+2]):
            u = p[:i+2]
            v = p[i+2:]
            break
    # u가 올바른 문자열이면 결과에 u + 1번부터 다시(v)
    if isCorrect(u):
        answer = u + solution(v)
    # 아니면 4번
    else:
        newStr = "("
        newStr += solution(v)
        newStr += ")"
        newStr += reverse(u)
        answer += newStr

    return answer

print(solution("))))(((("))