n = int(input())

student = []
for i in range(n):
    student.append(list(input().split()))

student.sort(key = lambda a : (-int(a[1]), int(a[2]), -int(a[3]), a[0]))  
for i in student:
    print(i[0])