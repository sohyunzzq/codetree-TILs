n = int(input())

pan = []
for i in range(n):
    pan.append([0]*n)

val = 1

if n % 2 == 0:
    index = 1
    while index < n:
        for i in range(n-1, -1, -1):
            pan[i][n-index] = val
            val += 1
        index += 1
        for i in range(n):
            pan[i][n-index] = val
            val += 1
        index += 1
else:
    index = 1
    while index != n:
        for i in range(n-1, -1, -1):
            pan[i][n-index] = val
            val += 1
        index += 1
        for i in range(n):
            pan[i][n-index] = val
            val += 1
        index += 1
    for i in range(n-1, -1, -1):
        pan[i][n-index] = val
        val += 1
    index += 1

for i in range(n):
    for j in range(n):
        print(pan[i][j], end = " ")
    print()