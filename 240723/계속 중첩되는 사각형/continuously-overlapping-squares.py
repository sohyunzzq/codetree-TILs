def paint(x1, y1, x2, y2, color):
    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = color

n = int(input())

area = []
for i in range(201):
    area.append([0]*201)

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    paint(x1+100, y1+100, x2+100, y2+100, i % 2)

cnt = 0
for i in range(201):
    for j in range(201):
        if area[i][j] == 1:
            cnt += 1
print(cnt)