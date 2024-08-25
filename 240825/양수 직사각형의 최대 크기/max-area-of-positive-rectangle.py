def check(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if area[i][j] < 0:
                return 0
    return (x2 - x1 + 1) * (y2 - y1 + 1)

def rectangle():
    maxi = 0
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    maxi = max(maxi, check(x1, y1, x2, y2))
    return maxi

n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

ans = rectangle()
if ans == 0:
    print(-1)
else:
    print(ans)