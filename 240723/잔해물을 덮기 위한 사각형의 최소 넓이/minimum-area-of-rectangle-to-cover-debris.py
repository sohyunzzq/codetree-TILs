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

result = 0

xmax, xmin, ymax, ymin = 0, 0, 0, 0
for i in range(2001):
    for j in range(2001):
        if area[i][j] == 1:
            xmax = max(i, xmax)
            xmin = min(i, xmin)
            ymax = max(j, ymax)
            ymin = min(j, ymin)
            result = (xmax - xmin + 1) * (ymax - ymin + 1)
print(result)