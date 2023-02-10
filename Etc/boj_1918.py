express = input()

result = ""
cal = []
for s in express:
    if s.isalpha(): # 알파벳이면 결과 추가
        result += s
    else:
        if s == '+' or s == '-': 
            while cal and cal[-1] != '(': # '+' 나 '-'면 '(' 나올때 까지 다 결과에 추가
                result += cal.pop()
            cal.append(s)
        elif s == '/' or s == '*': # '/' 나 '*'면 우선순위 같은 자기들 나올때 까지 뺌
            while cal and (cal[-1] == '*' or cal[-1] == '/'):
                result += cal.pop()
            cal.append(s)
        elif s == '(':
            cal.append(s)
        else:
            while cal[-1] != "(": # ')' 면 자기 짝 찾을때 까지 뺌
                result += cal.pop()
            cal.pop() # '(' 빼주기


while cal:
    result += cal.pop()
print(result)