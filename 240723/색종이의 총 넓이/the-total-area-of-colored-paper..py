def paste(x, y):
    for i in range(x, x+8):
        for j in range(y, y+8):
            area[i][j] = 1

n = int(input())

area = []
for i in range(201):
    area.append([0] * 201)

for i in range(n):
    x, y = map(int, input().split())
    paste(x, y)

cnt = 0
for i in range(201):
    for j in range(201):
        if area[i][j] == 1:
            cnt += 1
print(cnt)