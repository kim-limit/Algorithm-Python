def check(data, line):
    for i in range(3):
        col = ''
        row = ''
        for j in range(3):
            col += data[i + 3 * j]
            row += data[j + 3 * i]
        if col == line or row == line:
            return True
    if data[0] + data[4] + data[8] == line:
        return True
    if data[2] + data[4] + data[6] == line:
        return True
    return False
    
while True:
    data = input()
    if data == 'end': # end면 끝
        break

    cnt_o = data.count('O')
    cnt_x = data.count('X')

    if cnt_o == cnt_x: # o가 이겨야 유효함
        if check(data, 'OOO'):
            if check(data, 'XXX'):
                print('invalid')
            else:
                print('valid')
        else:
            print('invalid')
    elif cnt_o + 1 == cnt_x:
        if '.' in data:
            if check(data, 'XXX'):
                if check(data, 'OOO'):
                    print('invalid')
                else:
                    print('valid')
            else:
                print('invalid')
        else:
            if check(data, 'OOO'):
                print('invalid')
            else:
                print('valid')
    else:
        print('invalid')


