n = int(input())

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count+=1

# 24 * 60 * 60 = 86400 -> 완탐 가능
print(count)