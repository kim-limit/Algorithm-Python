s = input()

one_split = s.split('1')
zero_split = s.split('0')
one_split = [i for i in one_split if i != ""]
zero_split = [i for i in zero_split if i != ""]

print(min(len(one_split), len(zero_split)))