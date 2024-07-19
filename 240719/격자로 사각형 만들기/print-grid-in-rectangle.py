n = int(input())

pan = []
for i in range(n):
    pan.append([0]*n)

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            pan[i][j] = 1
        else:
            pan[i][j] += pan[i-1][j-1] + pan[i-1][j] + pan[i][j-1]

for i in pan:
    for j in i:
        print(j, end = " ")
    print()