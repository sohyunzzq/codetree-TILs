import sys
MAX_COOR = 400

n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

ans = sys.maxsize	

for i in range(n):
    area = []
    for j in range(MAX_COOR + 1):
        area.append([0] * (MAX_COOR + 1))
    
    for j in range(n): #순회
        if i == j:
            continue
        area[lst[j][0]][lst[j][1]] = 1
    
    minx, miny = sys.maxsize, sys.maxsize
    maxx, maxy = 0, 0
    for x in range(1, MAX_COOR + 1):
        for y in range(1, MAX_COOR + 1):
            if area[x][y] == 1:
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)
    
    ans = min((maxx - minx) * (maxy - miny), ans)

print(ans)