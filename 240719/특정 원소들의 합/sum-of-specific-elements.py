pan = []

for i in range(4):
    pan.append(list(map(int, input().split())))

sum1 = 0

for i in range(4):
    for j in range(i+1):
        sum1 += pan[i][j]

print(sum1)