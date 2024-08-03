import sys

n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

ans = sys.maxsize	

for i in range(n):
    for j in range(n): #순회
        if i == j:
            continue
    
    minx, miny = sys.maxsize, sys.maxsize
    maxx, maxy = 0, 0

    for j in range(n):
        if i == j:
            continue
        x = lst[j][0]
        y = lst[j][1]

        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    
    ans = min((maxx - minx) * (maxy - miny), ans)

print(ans)