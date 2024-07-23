def paint(x1, y1, x2, y2, num):
    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = num

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
mx1, my1, mx2, my2 = map(int, input().split())

area = []
for i in range(2001):
    area.append([0] * 2001)

paint(ax1, ay1, ax2, ay2, 1)
paint(bx1, by1, bx2, by2, 1)
paint(mx1, my1, mx2, my2, 2)

cnt = 0
for i in range(2001):
    for j in range(2001):
        if area[i][j] == 1:
            cnt += 1
print(cnt)