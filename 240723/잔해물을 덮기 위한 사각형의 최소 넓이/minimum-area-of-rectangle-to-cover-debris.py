def cover(x1, y1, x2, y2, num):
    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = num

r1x1, r1y1, r1x2, r1y2 = map(int, input().split())
r2x1, r2y1, r2x2, r2y2 = map(int, input().split())

area = []
for i in range(2001):
    area.append([0] * 2001)

cover(r1x1+1000, r1y1+1000, r1x2+1000, r1y2+1000, 1)
cover(r2x1+1000, r2y1+1000, r2x2+1000, r2y2+1000, 0)

a = -1
b = -1
c = -1
d = -1

flag = 0
for i in range(2001):
    if flag == 0:
        for j in range(2001):
            if area[i][j] == 1:
                a = i
                flag = 1
                break

flag = 0
for i in range(2000, -1, -1):
    if flag == 0:
        for j in range(2001):
            if area[i][j] == 1:
                b = i
                flag = 1
                break

flag = 0
for i in range(2001):
    if flag == 0:
        for j in range(2001):
            if area[j][i] == 1:
                c = i
                flag = 1
                break

flag = 0
for i in range(2000, -1, -1):
    if flag == 0:
        for j in range(2001):
            if area[j][i] == 1:
                d = i
                flag = 1
                break

if a == -1 or b == -1 or c == -1 or d == -1:
    print(0)
else:
    print((b-a+1) * (d-c+1))